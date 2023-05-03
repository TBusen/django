# Starting a New Project


Lorem ipsum dolor sit amet, (1) consectetur adipiscing elit.
{ .annotate }

1.  :man_raising_hand: I'm an annotation! I can contain `code`, __formatted
    text__, images, ... basically anything that can be expressed in Markdown.


## Set up virtual environment

```bash
conda create --name python=3.11 (1) some text
{.annotate}

1.  This can be ran on python 3.10 also
```

Now activate the environment and install required packages

```bash 
conda activate <name>
```

## Create new Project

Use Django Admin to create a new project

```bash
django-admin startproject <name>
```

This creates the project level directory and file structure which includes the site level manage.py and site level urls.py and settings.py.  The directory structure is 

```bash
|-- site_name
    |-- site_name
    |   |-- files
    |-- manage.py
```

CD into the new site directory and create application 

```bash 
cd site_name
```

```bash 
python manage.py startapp <app_name>
```
We've now added the structure 

```bash
|-- site_name
   |-- site_name
   |   |-- files
   |-- manage.py
   |-- app_name
       |-- models.py
       |-- views.py
       |- tests.py
```
## Register application

With the application structure generated we need to register it with Django.  This is done in the site level settings.py file.  Add the application name to the INSTALLED_APPS list.

```python
INSTALLED_APPS = [
    "school.apps.SchoolConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

## Setting up application

Setting up the application requires adding the following to the standard configuration from startapp

Create New templates directory and html files under app_name


```bash
|-- site_name
   |-- site_name
   |   |-- files
   |-- manage.py
   |-- app_name
       |-- templates
       |   |-- app_name
       |        |-- home.html
       |-- models.py
       |-- views.py
       |-- tests.py
```


For this example we will use home.html as a landing page which is now in our templates folder.  We need to create and connect your view to this template.

Inside the template we put a simple html string to render

```html
<h1>Welcome to home.html</h1>
```

Inside our application <mark>views.py </mark> we create a simple function-based view to render this template.

```python
def home_view(request):
    return render(request, 'classroom/home.html')
```

This function takes in a request and from django.shortcuts returns the rednderign of the request and points to 'classroom/home.html' which is in *app_name/templates/app_name/*

With the new view created we now need a urls.py file at the application level.

```bash
|-- site_name
   |-- site_name
   |   |-- files
   |-- manage.py
   |-- app_name
       |-- templates
       |   |-- app_name
       |        |-- home.html
       |-- models.py
       |-- views.py
       |-- tests.py
       |-- urls.py
```

```python
from django.urls import path
from .views import home_view

app_name = 'classroom'

urlpatterns = [
    path('', home_view, name='home')
]
```

A couple things to note here:

-  The view must be imported
-  The app_name must be registered
-  The path function expects a function (home_view)
-  py specifying '' this will route to *domain.com/classroom/*


We now need to connect our application level urls.py to the project (site) level urls.py

```bash
|-- site_name
   |-- site_name
   |   |-- urls.py
```

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('classroom/', include('classroom.urls'))
]
```

We need to add the import of *include*.  Add to the urlpatterns list a new path indicating the routing of *domain.com/classroom/* should reference classroom.urls which is referenced by the registered app_name *classroom* and will point to the application level urls.py, which now points to the home_view.

classroom url.py doesn't exist by default and you need to create it.  It is the same as the application level urls.py

```bash
|-- site_name
   |-- site_name
   |   |-- files
   |-- manage.py
   |-- app_name
       |-- templates
       |   |-- app_name
       |        |-- home.html
       |-- models.py
       |-- views.py
       |-- tests.py
       |-- urls.py
   |-- classroom
       |-- templates
       |   |-- classroom
       |        |-- home.html
       |-- models.py
       |-- views.py
       |-- tests.py
       |-- urls.py
```

The Contents of the application level urls.py (not site level) is:
    
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')]
```

No create the index function based view in views.py

```python
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'classroom/home.html')
```

!!! Note "Redirecting"
     If you want to redirect you can add this to urls.py.  In this example we redirect from home page to another page.
    ```python
    from django.views.generic import RedirectView

    #add this line to urlpatters
    path('', RedirectView.as_view(url='classroom/'))
    ```

### Create the model

We now want to create a model representing a teach.  This model is what will interact with our database.

The modified file is here:

```bash
|-- site_name
   |-- site_name
   |   |-- files
   |-- manage.py
   |-- app_name
       |-- templates
       |   |-- app_name
       |        |-- home.html
       |-- models.py
```

```python
from django.db import models


# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} teaches {self.subject}"
```

Give the model the attributes of first_name, last_name, and subject.  Add a string method to represent teacher.

With the new class defined we need to make migration and migrate for it to be reflected in the database.

```bash
python manage.py makemigrations
```

This only preps the migrations, it doesn't actually persist anything yet.

```bash
python manage.py migrate
```

Now it is migrated.

!!! warning "Undetected Migrations"

    If your application name is not defined under INSTALLED_APPS in settings.py then any changes will not be picked up with the above commands.


Verify that home.html is displaying by starting the dev server

```bash
python manage.py runserver 8080
```

## Generic Views

### TemplateView

Some views are very common and for those Django has generic views.  The work is repetitive (link view to template).  One of those views is template view.


```python
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
# def home_view(request):
#     return render(request, "classroom/home.html")


class HomeView(TemplateView):
    template_name = "classroom/home.html"
```
import the TemplateView class from django.  This is what your class-based view inherits.  What is required is to set the *template_name* variable to the template location.  There isn't much difference compared to the function-based view above in terms of simplicity, but the advantages will become more evident later.  

We have to now register this new class view with urls.py so that it can render

```python
from django.urls import path
#from .views import home_view
from .views import HomeView

app_name = "classroom"

urlpatterns = [
    #path("", home_view, name="home")
	path("", HomeView.as_view(), name="home")
    ]
```

Import the class inot urls.py.  Since *path* expects a function we just have to call the *as_view* method on the class to satisfy this.

Assuming a thank you page is created, how do we reference other pages?

Inside our home.html:

```html
<h1>Welcome to home.html</h1>

<ul>
	<li>
		<a href="{%url "classroom:thank_you"%}">Thank You Page Link</a>
	</li>
</us>

```

Using django templating, we use the %url magic.  "classroom:thank_you" is what we registered the thank you view under in url.py

```python
from django.urls import path

# from .views import home_view
from .views import HomeView, ThankYou

app_name = "classroom"

urlpatterns = [
    # path("", home_view, name="home")
    path("", HomeView.as_view(), name="home"),
    path("thank_you", ThankYou.as_view(), name="thank_you"),
]
```

!!! info "TemplateView Usage"
    TemplateView should really only be used when we expect most of the work to be done on the template side of things ie in the html

### FormView

First, create a simple form, here we are creating a new template called contact.html

```html
<h1>Contact Form Template</h1>

<form method="POST">
  {% csrf_token %}
   {{form.as_p}}
  <input type="submit" , value="submit" />
</form>
```

Next, create a new forms.py file for our classroom application.

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
```

Finally, connect to the new form view

```python
class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "classroom/contact.html"

    # success URL?
    success_url = '/classroom/thank_you/'

    # what do do with form
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
```
form_class is the name of your form class in forms.py.  Template name is the name of the html template to render.  success_url is the actual url path to go after success of the form submission, this is not the template path.  Then, create a form_valid method to define what to do with the actual form.  Here we are just printing the cleaned_data and then returning the valid form data using the form_valid method inherited from FormView.

!!! note "Using Reverse Lazy"
    if you instead want to refer to the url routing then you can use reverse_lazy

    ```python
     success_url = reverse_lazy("classroom:thank_you")
     ```

As a last step, link the new view in urls.py

```python
urlpatterns = [
    # path("", home_view, name="home")
    path("", HomeView.as_view(), name="home"),
    path("thank_you/", ThankYou.as_view(), name="thank_you"),
    path("contact/", ContactFormView.as_view(), name="contact"),
]
```

### CreateView

> This is a model-based view, meaning that it will connect and directly interact with our backend.


```python
class TeacherCreateView(CreateView):
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy("classroom:thank_you")
```

Import the *Teacher* model from classroom.models and *CreateView* from django.views.generic.  This CBV will connect to the Teacher model and make available all fields.  Using reverse_lazy we will be redirected to the thank you page if successful.

How does this CBV know which html file to look for?  The pattern it is looking for is **model_form.html**, so in this case we need to have a teacher_form.html file.

In our teacher_form.html we would have the following:

```html
<h1>Teacher Form</h1>
<form method="POST">
  {% csrf_token %}
   {{form.as_p}}
  <input type="submit" value="Submit" />
</form>
```

### ListView

Now that we have our CBV, we will create a List view to show the contents of this table.

```python
class TeacherListView(ListView):
    # looking for model_list.html
    model = Teacher
```
Import ListView and create a new CBV.  Inherit from ListView.  The only thing that needs referenced is the Model, which is Teacher in our example.  This wil be looking for template of the pattern model_list.html.

Lets create our teacher_list.html view now.

```html
<h1>Teacher List View</h1>
<ul>
  {% for teacher in object_list %}

  <li>{{teacher.first_name}} {{teacher.last_name}}</li>
  {% endfor %}
</ul>
```

Now reference the new view in urls.py.

```python
urlpatterns = [
    # path("", home_view, name="home")
    path("", HomeView.as_view(), name="home"),
    path("thank_you/", ThankYou.as_view(), name="thank_you"),
    path("contact/", ContactFormView.as_view(), name="contact"),
    path("create_teacher/", TeacherCreateView.as_view(), name="create_teacher"),
    path("list_teacher/", TeacherListView.as_view(), name="list_teacher"),

]
```

Finally, add the teacher page to the home page list items

```html
	<li>
			<a href="{%url "classroom:list_teacher"%}">List Teacher Page Link</a>
		</li>
```

We can change the "object_list" name as so

```python
class TeacherListView(ListView):
    # looking for model_list.html
    model = Teacher
    context_object_name = "teacher_list"
```

Now reference teacher_list in our for loop inside teacher_list.html template

```html
<h1>Teacher List View</h1>
<ul>
  {% for teacher in teacher_list %}

  <li>{{teacher.first_name}} {{teacher.last_name}}</li>
  {% endfor %}
</ul>
```

We can override the default query behavior

```python
class TeacherListView(ListView):
    # looking for model_list.html
    model = Teacher
    context_object_name = "teacher_list"
    #default query set
    #queryset = Teacher.objects.all()
    queryset = Teacher.objects.order_by('first_name')
```

### DetailView

This view allows you to pull a single row from the object given a PK

```python
class TeacherDetailView(DetailView):
    model = Teacher
    context_object_name = "teacher"
```

Setting up the view only requires the model to be referenced.  The template that will be used is the pattern model_detail.html.  So in this case we need to create a teacher_detail.html file.

```html
<h1>Teacher Detail View</h1>
{{teacher}}
```

Setting up the template of the required pattern and then reference the contect object name in the template.  In this case we are referencing the teacher object.

Now modify the teacher list view to be urls pointing to the detail view.

```html
<h1>Teacher List View</h1>
<ul>
  {% for teacher in teacher_list %}

  <li>
    <a href="/classroom/teacher_detail/{{teacher.id}}"
      >{{teacher.first_name}} {{teacher.last_name}}</a
    >
  </li>

  {% endfor %}
</ul>
```

We loop through the rows in the teacher object pulling the pk and passing that into the url setup in urls.py for the detail view


```python
urlpatterns = [
    # path("", home_view, name="home")
    path("", HomeView.as_view(), name="home"),
    path("thank_you/", ThankYou.as_view(), name="thank_you"),
    path("contact/", ContactFormView.as_view(), name="contact"),
    path("create_teacher/", TeacherCreateView.as_view(), name="create_teacher"),
    path("list_teacher/", TeacherListView.as_view(), name="list_teacher"),
    path("teacher_detail/<int:pk>/", TeacherDetailView.as_view(), name="teacher_detail"),
]
```

### UpdateView

This view allows you to update a single row from the object given a PK

```python
class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy("classroom:list_teacher")
```

We need to import UpdateView from django.views.generic.  We need to reference the model, in this case Teacher.  We need to reference the fields that we want to be able to update.  We need to reference the success url, in this case we want to be redirected to the list view.

No we need to update urls.py to include the new view in urls.py

Import the view and add the path to the url

```python
from .views import (
    HomeView,
    ThankYou,
    ContactFormView,
    TeacherCreateView,
    TeacherListView,
    TeacherDetailView,
    TeacherUpdateView,
)
```


```python
urlpatterns = [
    # path("", home_view, name="home")
    path("", HomeView.as_view(), name="home"),
    path("thank_you/", ThankYou.as_view(), name="thank_you"),
    path("contact/", ContactFormView.as_view(), name="contact"),
    path("create_teacher/", TeacherCreateView.as_view(), name="create_teacher"),
    path("list_teacher/", TeacherListView.as_view(), name="list_teacher"),
    path("teacher_detail/<int:pk>/", TeacherDetailView.as_view(), name="teacher_detail"),
    path("teacher_update/<int:pk>/", TeacherUpdateView.as_view(), name="teacher_update"),
]
```

Now we need to expose this view in the list view b/c this temaplate is already exposing the pk in the for loop.  We will add another anchor tag with an option to update the teacher.

```html
<h1>Teacher List View</h1>
<ul>
  {% for teacher in teacher_list %}

  <li>
    <a href="/classroom/teacher_detail/{{teacher.id}}"
      >{{teacher.first_name}} {{teacher.last_name}}</a
    >
    <a href="/classroom/teacher_update/{{teacher.id}}"
      >Update Teacher for {{teacher.first_name}}</a
    >
  </li>

  {% endfor %}
</ul>
```

Start the server to test the update view.

```bash
python manage.py runserver
```


### DeleteView

This allows you to delete a single row from the object given a PK

Import DeleteView from django.views.generic

```python
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
```

Create the view in views.py.  Note that you also need to create a template with the naming `model_confirm_delete.html`

```python
class TeacherDeleteView(DeleteView):
    # Form --> Confirm Delete --> Delete
    model = Teacher
    # reroute to teacher list to ensure the teacher is deleted
    success_url = reverse_lazy("classroom:list_teacher")
```

Create your template `teacher_confirm_delete.html`

```html
<h1>Are you sure you want to delete this teacher?</h1>
<h2>{{teacher}}</h2>

<form method="POST">
  {% csrf_token %}
  <input type="submit" value="Confirm Delete" />
</form>
```

All that is needed is a simple form with a submit button.  The form will be a POST request and will need a csrf token.  Optionally, we can add a H2 showing the current teach object about to be deleted.

Add the path to urls.py

```python
urlpatterns = [
    # path("", home_view, name="home")
    path("", HomeView.as_view(), name="home"),
    path("thank_you/", ThankYou.as_view(), name="thank_you"),
    path("contact/", ContactFormView.as_view(), name="contact"),
    path("create_teacher/", TeacherCreateView.as_view(), name="create_teacher"),
    path("list_teacher/", TeacherListView.as_view(), name="list_teacher"),
    path("teacher_detail/<int:pk>/", TeacherDetailView.as_view(), name="teacher_detail"),
    path("teacher_update/<int:pk>/", TeacherUpdateView.as_view(), name="teacher_update"),
    path("teacher_delete/<int:pk>/", TeacherDeleteView.as_view(), name="teacher_delete"),
]
```

## Create the models

Populate the models for the Library application.  We will have models for Author, Book, and Publisher, etc.  Create these in the models.py file.

```python
class Genre(models.Model):
    # this is a model representing a book genre

	name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

	def __str__(self):
		# string for representing the Model object
		return self.name
```

Example of a model for Genre.  Genre inherits from models.model.  `models` is imported.  We have a single field, name, which is a CharField with a max length of 200.  We have a help text for the field.  We have a `__str__` method that returns the name of the genre.

Another example

```python
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # date of birth and death are optional
    date_of_birth = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ["last_name", "first_name"]
        
    def get_absolute_url(self):
		# returns the url to access a particular author instance
        return reverse("author_detail", kwargs={"pk": self.pk})
        
    def __str__(self):
		# string for representing the Model object
        return f"{self.last_name}, {self.first_name}"
```

The Author model has a first_name and last_name field.  The date_of_birth is optional.  We have a Meta class that will order the last_name and first_name.  We have a `get_absolute_url` method that will return the url to access a particular author instance.  We have a `__str__` method that will return the last_name, first_name.  Notice the get_absolute_url takes the primary key as an argument and then returns the url for the author_detail view.


When models are complete you need to make mygrations and migrate

```bash
python manage.py makemigrations
python manage.py migrate
```

Next Step is to Register the models, create teh super user and create example instances


register the model in admin.py

```python
from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)
```


create the superuser

```bash
python manage.py createsuperuser
```


Start the server and log into the admin panel

```bash
python manage.py runserver
```


After using the admin pane to populate data for the views and create a book instance we need to set up the views

in views.py

```python
class BookCreate(CreateView):  # book_form.html
    model = Book
    fields = "__all__"
    # initial = {"date_of_death": "05/01/2018"}
    ```

By default when a book is created it will redirect to the detail view.  We can change this by adding a `get_absolute_url` method to the model.  This will redirect to the detail view after the book is created.  However, we will create the detail view instead

```python
class BookDetailView(DetailView):
    model = Book
```

We need templates for these views.  Django expects the pattern, model_viewtype.html.  So we need book_form.html and book_detail.html

```bash
touch templates/catalog/book_form.html && touch templates/catalog/book_detail.html
```

A simple form

```html
<h1>Create New Book</h1>

<form action="" method="post">
  {% csrf_token %} {{ form.as_p }}
  <input type="submit" value="Create Book" />
</form>

```

And then dump the object in the detail template

```html
<h1>Book Detail that doesn't show detail</h1>
{{book}}
```

!!! Note "Context Variables"
    Take note that the object name is lowercase.  This is because the object is passed to the template as a context variable.  The context variable is the lowercase version of the model name.  So if the model is Book, the context variable is book.  If the model is Author, the context variable is author.


## Security / User Model and Authentication

Now that the site works.  We can add and view books, lets restrict who can do this.

Step 1:  Create Groups

In the admin panel, create two groups, Librarians and Patrons

Step 2: Create users and put them in the groups

In the admin panel create the user, save adn then add to the Partron groups.


Now go to url.py for project level.  Include the django.contrib.auth.urls

```python

urlpatterns = [
    path("admin/", admin.site.urls),
    path("catalog/", include("catalog.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]
```

To access this you go to url/accounts/login.  But you will get an error because we do not have a template set up.  Lets create that.  This authentication happens at a site level, not application.  So create a new template folder at the project level.

```bash
|-- library
|   |-- catalog
|   |-- library
|   |-- templates
|   |   |-- registration
|   |   |   |-- login.html
```

add the following to the settings.py file

```python
import os

# under TEMPLATES
TEMPLATES = [
    {
        "DIRS": [os.path.join(BASE_DIR, "templates")],

    }
]
```

The login template needs to take in a couple different cases

- Incorrect Login Params
- Logged in but not authorized to view the page
- Logged in and authorized to view the page

```html
{% if form.errors %}<p>Your username and password was incorrect. Try again</p>{% endif %}
{% if next %}
    {% if user.is_authenticated %}
        <p>You don't have permission for this page</p>
    {% else %}
        <p>Please login to see this page</p>
    {% endif %}
{% endif %}
<form action="{% url 'login' %}" method="post">
    {% csrf_token %}
    {{ form.username.label_tag }}}
    {{ form.username }}
    {{ form.password.label_tag }}
    {{ form.password }}
	<input type="submit" value="Login">
	<input type="hidden" name="next" value="{{ next }}>
</form>
```

- If there are errors on the form, return a message to try again
- If `next` which means they are passed to the next page
  - If the user is authenticated they get the message that they can't see the page
  - Other wise they get the message to login to see the page
- Otherwise they get the login form


Logging in, Django automatically redirects you to /acounts/profile.  You can create this or define your own redirect in settings.py

```python
LOGIN_REDIRECT_URL = "/"
```

Now that authentication and redirect work, we need to decorate view to have them require or not require a user to be authenticated

To do this, you use decorators for function based views and mixins for class based views


When logged in or logged out you can add next? routing so that they stay on current page when logged in or out

```html
<a href="{% url 'login' %}?next={{ request.path }}">Login</a>
```


### Function Based Views

First create a function based view

```python
    def my_view(request):
    return render(request, "catalog/my_view.html")
 ```

 Create my_view.html

```html
<h1>LOGGED IN USERS ONLY!</h1>
```

To restrict this based on security decorate the function

```python
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    return render(request, "catalog/my_view.html")


# register the view in urls.py
urlpatterns = [
    path("my_view/", views.my_view, name="my-view"),
]
```

For Class based view use a mixing

```python
from django.contrib.auth.mixins import LoginRequiredMixin

class BookCreate(LoginRequiredMixin, CreateView):  # book_form.html
    model = Book
    fields = "__all__"
    # initial = {"date_of_death": "05/01/2018"}
```

## User Authentication Forms

You can use the built in "User" object for authentication, but you can also create your own model and form for authentication.  This is useful if you want to add additional fields to the user model.

To use the built in user model we need to import the form


```python
    from django.contrib.auth.forms import UserCreationForm
```

Then we can use this form in the view
 
```python
    class SignUp(CreateView):
        form_class = UserCreationForm
        success_url = reverse_lazy("login")
        template_name = "catalog/signup.html"
```

Catalog/signup.html doesn't exist yet, so create it

```html
<h1>Sign Up</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Sign Up</button>
</form>
```

Register with urls.py

```python
    path("signup/", views.SignUp.as_view(), name="signup"),
```

## User Page Permissions

