from django.urls import path
from my_app import views

#register app namespace
app_name = 'my_app'


urlpatterns = [
    path('', views.example_view, name='example'), # domain.com/my_app/
    path('variable/', views.variable_view, name='variable')
]
