from django.urls import path
from first_app import views

# domain.com/first_app
urlpatterns = [
    path('', views.simple_view)
]