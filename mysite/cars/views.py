from django.shortcuts import render, redirect
from .forms import ReviewForm
from django.urls import reverse

# Create your views here.
def rental_review(request):

    if request.method=='POST':
        form=ReviewForm(request.POST)
        #enforce rules like length check
        if form.is_valid():
            form.save()
            return redirect(reverse('cars:thank_you'))
    else:
        form = ReviewForm()
    return render(request, 'cars/rental_review.html', context={'form':form})


def thank_you(request):
    return render(request, 'cars/thank_you.html')