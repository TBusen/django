from django.shortcuts import render
from django.http import HttpResponse
from .models import *  # import all models from models.py but you should list them specifically
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm  # model form not a view
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    # return render(request, "templates/index.html")
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact="a").count()

    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
    }

    return render(request, "catalog/index.html", context=context)


class BookCreate(LoginRequiredMixin, CreateView):  # book_form.html
    model = Book
    fields = "__all__"
    # initial = {"date_of_death": "05/01/2018"}


class BookDetail(DetailView):  # book_detail.html
    model = Book


# testing a function based view security
@login_required
def my_view(request):
    return render(request, "catalog/my_view.html")


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "catalog/signup.html"
