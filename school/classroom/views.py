from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from classroom.forms import ContactForm
from django.urls import reverse_lazy


# Create your views here.
# def home_view(request):
#     return render(request, "classroom/home.html")


class HomeView(TemplateView):
    template_name = "classroom/home.html"


class ThankYou(TemplateView):
    template_name = "classroom/thank_you.html"


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
