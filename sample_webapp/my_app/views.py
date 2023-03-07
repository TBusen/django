from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("HELLO THIS IS A VIEW INSIDE MY_APP ")
