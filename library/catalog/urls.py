from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_book/", views.BookCreate.as_view(), name="create_book"),
    path("book/<int:pk>/", views.BookDetail.as_view(), name="book_detail"),
    path("my_view/", views.my_view, name="my_view"),  # catalog/my_view.html
    path("signup/", views.SignupView.as_view(), name="signup"),
]
