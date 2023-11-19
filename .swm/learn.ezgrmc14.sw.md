---
id: ezgrmc14
title: Learn
file_version: 1.1.3
app_version: 1.18.32
---

The difference between using an empty \`\*\*action\*\*\` attribute (\``action=""`\`) and specifying a URL with \``{% url 'submit_form' %}`\` in the \`\*\*action\*\*\` attribute lies in how the form data is submitted and processed in a Django application.<br/>
1\. \*\*Empty \`action\` Attribute (\`\*\*\*\*`action=""`\*\*\`):<br/>
If the \`\*\*action\*\*\` attribute is empty, the form data will be submitted to the same URL as the one that displayed the form. This is useful when the form processing view is associated with the same URL where the form is displayed. In this case, the form will be submitted back to the current URL, and it's the responsibility of your Django view to handle the form submission at that URL.<br/>
Example:

`<form action="" method="post"><br/> <input type="submit" value="Submit"><br/> </form>`<br/>
<br/>In this case, you would typically have a Django view associated with the URL where this form is displayed, and that view would handle both the GET and POST requests for that URL.<br/>
2\. \*\*Specifying a URL with \`\*\*\*\*`{% url 'submit_form' %}`\*\*\`:<br/>
If you specify a URL using the \``{% url 'submit_form' %}`\` template tag in the \`\*\*action\*\*\` attribute, the form data will be submitted to the URL associated with the named URL pattern \\\`'submit\\\_form'\\\`. This is useful when you want to explicitly define a separate URL for handling form submissions, and you have a dedicated view for processing form data.<br/>
Example:

`<form action="{% url 'submit_form' %}" method="post"><br/> {% csrf\_token %}<br/> <input type="submit" value="Submit"><br/> </form>`<br/>
In this case, the form data will be submitted to the URL associated with the named URL pattern '`submit_form`', and you would have a Django view specifically designed to handle the form submission at that URL.<br/>
In summary, using an empty \`\*\*action\*\*\` attribute submits the form to the current URL, while specifying a URL with \``{% url 'submit\_form' %}`\` submits the form to a specific URL associated with a named URL pattern in your Django project. The choice depends on the design of your application and how you've structured your views and URL patterns.
<!-- NOTE-swimm-snippet: the lines below link your snippet to Swimm -->
### 📄 templates/signup.html
```html
31                 <form action="" method="POST">
```

<br/>

In a Django view function, when a form is submitted, you can access the form data through the `request` object. The `name` attributes of the form fields are crucial because they determine the keys under which the form data is stored in the `request.POST` dictionary.

Here's an example of how you might handle the form submission in a Django view:

Assuming you have a Django view function named `signup`:

```python
from django.shortcuts import render
from django.http import HttpResponse

def signup(request):
    if request.method == 'POST':
        # Retrieve form data using the 'name' attributes
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('/')
        password2 = request.POST.get('password2')

        # Perform your form validation and processing here
        # For simplicity, let's just print the form data for now
        print(f'Email: {email}')
        print(f'Username: {username}')
        print(f'Password: {password}')
        print(f'Repeat Password: {password2}')

        # Add your logic for user registration or other actions

        return HttpResponse('Form submitted successfully!')
    else:
        # Render the form template for GET requests
        return render(request, 'your_app/your_template.html')
```

In this example, when the form is submitted, the view checks if the request method is `POST`. If it is, the view retrieves the form data using `request.POST.get('field_name')`, where `'field_name'` corresponds to the `name` attribute of each input field in the HTML form. The form data is then processed as needed. For simplicity, the example just prints the form data, but you would typically use this data for user registration or other actions in a real-world application.

Remember to replace `'your_app/your_template.html'` with the actual path to your template.

Also, keep in mind that this example lacks proper form validation and security measures. In a production environment, you would want to implement additional validation and use Django forms for handling user input securely.
<!-- NOTE-swimm-snippet: the lines below link your snippet to Swimm -->
### 📄 templates/signup.html
```html
33                     <input type="email" name="email" placeholder="Email address" />
```

<br/>

CSRF stands for Cross-Site Request Forgery, and it is a type of attack where a malicious website tricks a user's browser into making an unintended request to a different site. To prevent CSRF attacks, Django includes a built-in mechanism called CSRF protection, and the CSRF token is a key component of this security feature.

Here's how CSRF protection works in Django:

1.  **Token Generation:** When a Django form containing the `{% csrf_token %}` template tag is rendered, a unique CSRF token is generated by Django. This token is specific to the user's session.

    ```python
    <form method="post">
        {% csrf_token %}
        <!-- Other form fields go here -->
        <input type="submit" value="Submit">
    </form>
    ```

2.  **Inclusion in Form Submissions:** The generated CSRF token is included in the HTML form as a hidden input field. When the user submits the form, the token is sent along with the other form data.

3.  **Verification in the Server:** Upon receiving a form submission, Django checks if the submitted CSRF token matches the one associated with the user's session. If the tokens don't match or if the token is missing, Django considers the request potentially malicious and rejects it.

By verifying that the CSRF token in the form submission matches the one associated with the user's session, Django ensures that the form was submitted by the user from the same site and not by a malicious third party.

To include the CSRF token in your Django forms, you can use the `{% csrf_token %}` template tag, as shown in the example above. This tag inserts an `<input>` field with the name `'csrfmiddlewaretoken'` and a value representing the unique token.

It's important to always include the `{% csrf_token %}` tag in your forms when using the POST method to submit data in Django, as it helps protect your application from CSRF attacks. Django's CSRF protection is enabled by default in the middleware settings (`'django.middleware.csrf.CsrfViewMiddleware'`).
<!-- NOTE-swimm-snippet: the lines below link your snippet to Swimm -->
### 📄 templates/signup.html
```html
32                     {% csrf_token %}
```

<br/>

The two code snippets you provided define a tuple and a list, respectively, both containing choices for a Django model field. Let's break down the differences:

1. **Tuple Definition:**
    ```python
    GENRE_CHOICES = (
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('thriller', 'Thriller'),
    )
    ```

2. **List Definition:**
    ```python
    GENRE_CHOICES = [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('thriller', 'Thriller'),
    ]
    ```

**Key Differences:**

- **Syntax:**
  - The first one uses parentheses, indicating that it's a tuple.
  - The second one uses square brackets, indicating that it's a list.

- **Immutability:**
  - Tuples are immutable, which means once they are defined, their elements cannot be changed or modified. In this case, the `GENRE_CHOICES` tuple cannot be altered.
  - Lists, on the other hand, are mutable, and you can modify their elements after they are created.

- **Use Case:**
  - For Django model choices, either a tuple or a list can be used. Django doesn't care if it's a tuple or a list. Both are iterable and can be used as choices for model fields.

- **Preference:**
  - Some developers prefer using tuples for choices because they are immutable and provide a clear indication that the data should not be changed.
  - Others might use lists if they anticipate the need to modify the choices later.
<!-- NOTE-swimm-snippet: the lines below link your snippet to Swimm -->
### 📄 core/models.py
```python
9          GENRE_CHOICES = (
10             ('action', 'Action'),
11             ('comedy', 'Comedy'),
12             ('drama', 'Drama'),
13             ('horror', 'Horror'),
14             ('romance', 'Romance'),
15             ('thriller', 'Thriller'),
16         )
```

<br/>

This file was generated by Swimm. [Click here to view it in the app](https://app.swimm.io/repos/Z2l0aHViJTNBJTNBbmV0ZmxpeCUzQSUzQWp1bmFpZDEwMTQ0/docs/ezgrmc14).
