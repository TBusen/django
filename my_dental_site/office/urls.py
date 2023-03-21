from django.urls import path
from office import views


urlpatterns = [
    path('', views.list_patients, name='list_patients')
]