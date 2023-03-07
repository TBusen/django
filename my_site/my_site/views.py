from django.http import HttpResponse


def home_view(request):
    return HttpResponse("this is home :-)")