from django.urls import path
from my_app import views


urlpatterns = [
    path('', views.example_view), # domain.com/my_app/
    path('variable/', views.variable_view)
]
