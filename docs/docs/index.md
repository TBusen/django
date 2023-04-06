# Starting a New Project
<br>
<br>

## Set up virtual environment

```bash
conda create --name python=3.11
```
<br>
<br>

Now activate the environment and install required packages

```bash 
conda activate <name>
```

## Create new Project
<br>
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
<br>

Setting up the application requires adding the following to the standard configuration from startapp

<br>
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

<br>

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

``bash
python manage.py migrate
```
Now it is migrated.

!!! warning Undetected Migrations

    If your application name is not defined under INSTALLED_APPS in settings.py then any changes will not be picked up with the above commands.



!!! note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.