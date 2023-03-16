from django.urls import path
from first_app import views


urlpatterns = [path('', views.simple_view)]  # domain.com/first_app
