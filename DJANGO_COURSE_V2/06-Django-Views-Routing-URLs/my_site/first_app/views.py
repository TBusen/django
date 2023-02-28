from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.

# ROUTES AND URLs LECTURE



# # BASIC FUNCTION VIEWS LECTURE
def simple_view(request):
    # return HttpResponse('SIMPLE VIEW!')
    return render(request,'first_app/example.html')


# DYNAMIC VIEWS AND VIEW LOGIC LECTURE

def add_view(request,num1,num2):
    result = num1+num2
    return HttpResponse(str(result))


articles = {
    "sports":"Welcome to the sports page",
    "finance":"Finance news here",
    "politics":"Politics is in the news"
}


# def news_view(request,topic):
#     headline = f"<h1>{articles[topic]}</h1>"
#     return HttpResponse(headline)

# REDIRECTS AND 404s LECTURE


def news_view(request,topic):
    try:
        headline = f"<h1>{articles[topic]}</h1>"
        return HttpResponse(headline)
    except:
        headline = "<h1>No article page for that topic!</h1>"
        return HttpResponseNotFound(headline)


pages = ['sports','finance','politics']
# REDIRECTS
def page_num_view(request,page_number):
    # domain.com/first_app/1 ----> domain.com/first_app/finance
    topic = pages[page_number]
    return HttpResponseRedirect(topic)

def num_page_view(request,num_page):

    topics_list = list(articles.keys()) # ['sports','finance','politics']
    topic = topics_list[num_page]

    
    return HttpResponseRedirect(reverse('topic-page',args=[topic]))
