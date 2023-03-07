from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index') # /my_app --> PROJECT urls.py
]