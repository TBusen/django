from django.shortcuts import render
from django.http.response import HttpResponse


articles = {
    "sports": "Sports Page",
    "finance": "Finance Page",
    "politics": "Politics Page",
}


def simple_view(request):
    return HttpResponse("Simple View in First_App")


#def sports_view(request):
#    return HttpResponse(articles.get("sports"))


#def finance_view(resquest):
#    return HttpResponse(articles.get("finance"))

def news_view(request, topic: str):
    return HttpResponse(articles.get(topic))

def add_view(request, num1: int, num2: int):
    #domain.com/first_app/3/4 --> 7
    result = num1 + num2
    return HttpResponse((str(result)))
