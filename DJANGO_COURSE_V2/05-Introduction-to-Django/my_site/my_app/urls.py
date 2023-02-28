from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.index,name='index') #/my_apps --> PROJECT urls.py
]