from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("logout", views.logout, name="logout"),
    path("movie/<str:movie_id>/", views.movie, name="movie"),
    path("add-to-list", views.add_to_list, name="add_to_list"),
]
