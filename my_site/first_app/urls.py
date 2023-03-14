from django.urls import path
from first_app import views

# domain.com/first_app
urlpatterns = [
    path('', views.simple_view),

    path('<topic>/', views.news_view),
    path('<int:num1>/<int:num2>', views.add_view)
]