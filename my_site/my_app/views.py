from django.shortcuts import render
from django.http    import HttpResponse

# Create your views here.


def example_view(request: str) -> HttpResponse:
    # my_app/templates/my_app/example.html

    return render(request, 'my_app/example.html')


def variable_view(request: str) -> HttpResponse:
    # my_app/templates/my_app/variable.html

    my_var = {'first_name': 'RosalInd', 'last_name': 'FrankLin',
              'some_list':[1,2,3], 'user_logged_in': False}

    return render(request, 'my_app/variable.html', context=my_var)
