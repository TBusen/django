# Starting a New Project

## Set up virtual environment

```bash
conda create --name python=3.11
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


Next register the application config in the site level settings.py.  This name can be found in the application-level *apps.py*

In this file we see this

```python
class ClassroomConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "classroom"
```

Copy and paste the name <mark>ClassroomConfig</mark> and then register this in *site_name/settings.py* under INSTALLED_APPS

ClassroomConfig

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```
add the following
```python
'classroom.apps.ClassroomConfig'
```
```python
INSTALLED_APPS = [
    'classroom.apps.ClassroomConfig',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
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
