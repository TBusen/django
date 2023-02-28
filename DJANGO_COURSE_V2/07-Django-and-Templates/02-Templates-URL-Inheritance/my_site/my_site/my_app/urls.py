from django.urls import path
from . import views

# Register the app namespace
app_name = 'my_app'

urlpatterns = [
    path('', views.example_view,name='home'),
    path('filters/',views.filter_view)
]
