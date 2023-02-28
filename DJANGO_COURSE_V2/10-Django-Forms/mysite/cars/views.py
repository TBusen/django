from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ReviewForm
# Create your views here.
def rental_review(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReviewForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            # Save Form to Models
            form.save()
            # redirect to a new URL:
            return redirect(reverse('cars:thank_you'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReviewForm()
        # context = 

    return render(request,'cars/rental_review4.html',context={'form':form})

def thank_you(request):
    return render(request,'cars/thank_you.html')

