from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, ListView
from classroom.forms import ContactForm
from django.urls import reverse_lazy
from classroom.models import Teacher


# Create your views here.
# def home_view(request):
#     return render(request, "classroom/home.html")


class HomeView(TemplateView):
    template_name = "classroom/home.html"


class ThankYou(TemplateView):
    template_name = "classroom/thank_you.html"


# create a create view ie create new teacher
class TeacherCreateView(CreateView):
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy("classroom:thank_you")


class TeacherListView(ListView):
    # looking for model_list.html
    model = Teacher
    context_object_name = "teacher_list"


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "classroom/contact.html"

    # success URL?
    # success_url = "/classroom/thank_you/"
    success_url = reverse_lazy("classroom:thank_you")

    # what do do with form
    def from_valid(self, form):
        print(form.cleaned_data["name"])
        return super().form_valid(form)
