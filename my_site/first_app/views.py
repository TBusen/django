from django.shortcuts import render


def simple_view(request):
    return render(request, 'first_app/example.html')
