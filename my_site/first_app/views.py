from django.shortcuts import render
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse



articles = {
    "sports": "Sports Page",
    "finance": "Finance Page",
    "politics": "Politics Page",
}


def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        raise Http404(("404 generic Error"))

#domain.com/first_app/0 --> domain.com/first_app/sports

def num_page_view(request, num_page):

    topics_list = list(articles.keys())
    topic = topics_list[num_page]
    webpage = reverse('topic-page', args=[topic]) # refer to url name and pass in args
    return HttpResponseRedirect(webpage)

