from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.views.generic import TemplateView, CreateView,DetailView, FormView,ListView,UpdateView,DeleteView
from classroom.models import Teacher
from classroom.forms import ContactForm
# Create your views here.

class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'

class ContactFormView(FormView):
    # Specify form to use (do not create an instance of the form!)
    form_class = ContactForm
    # Point to template to pass form
    template_name = 'classroom/contact.html'
    # Where to go upon valid form completion
    # DO NOT FORGET THE FIRST /
    # NOTE THIS IS A URL, NOT A TEMPLATE .HTML!!
    # success_url = '/classroom/thank_you/'
    # https://stackoverflow.com/questions/48669514/difference-between-reverse-and-reverse-lazy-in-django
    success_url = reverse_lazy('classroom:thank_you')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
         
        # Do stuff with form here! 
        # form.save() if ModelForm
        print(form.cleaned_data)
        return super().form_valid(form)

    

class TeacherCreateView(CreateView):
    # AUTO CONNECTS TO A TEMPLATE WITH THE NAME:
    # model_form.html
    # Make sure to match this template name schema!!
    model = Teacher
    # fields = ['name']
    fields = '__all__'

    success_url = reverse_lazy('classroom:thank_you')

class TeacherListView(ListView):
    model = Teacher 
    # Peform any .filter() you want here to only list certain items
    queryset = Teacher.objects.order_by('first_name')
    # customize the name of the object_list sent to template
    context_object_name = 'object_list'

class TeacherUpdateView(UpdateView):
    # Note! Uses model_form.html file as well
    # same form as CreateView
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy('classroom:list_teacher') 

class TeacherDeleteView(DeleteView):
    # Requires model_confirm_delete.html template name
    model = Teacher
    success_url = reverse_lazy('classroom:list_teacher')

class TeacherDetailView(DetailView):
    model = Teacher 
    # uses template with model_detail.html schema
