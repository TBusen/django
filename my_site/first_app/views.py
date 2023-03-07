from django.shortcuts import render
from django.http import HttpResponse

def simple_view(request):
    return HttpResponse("Simple View in First_App")
