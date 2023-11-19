from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Movie, MovieList
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import re


# Create your views here.
@login_required(login_url="/login")
def index(request):
    movies = Movie.objects.all()
    context = {
        "movies": movies,
    }
    return render(request, "index.html", context)


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # authenticate user
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid credentials")
            return redirect("login")
    return render(request, "login.html")


def signup(request):
    if request.method == "POST":
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect("signup")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect("signup")
            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email
                )
                user.save()

                # log user in
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                return redirect("/")
        else:
            messages.info(request, "Password not matching")
            return redirect("signup")
    else:
        return render(request, "signup.html")


@login_required(login_url="/login")
def movie(request, movie_id):
    movie_details = Movie.objects.get(uu_id=movie_id)

    context = {
        "movie_details": movie_details,
    }

    return render(request, "movie.html", context)


def add_to_list(request):
    if request.method == "POST":
        movie_url_id = request.POST.get("movie_id")
        uuid_pattern = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
        match = re.search(uuid_pattern, movie_url_id)
        movie_id = match.group() if match else None

        movie = get_object_or_404(Movie, uu_id=movie_id)
        movie_list, created = movie_list.objects.get_or_create(
            owner_user=request.user, movie=movie
        )

        if created:
            resonse_data = {"status": "success", "message": "Added ✓"}
        else:
            resonse_data = {"status": "info", "message": "Movie Already in list"}

        return JsonResponse(resonse_data)
    else:
        return JsonResponse(
            {"status": "error", "message": "Invalid Request"}, status=400
        )


@login_required(login_url="login")
def logout(request):
    auth.logout(request)
    return redirect("login")
