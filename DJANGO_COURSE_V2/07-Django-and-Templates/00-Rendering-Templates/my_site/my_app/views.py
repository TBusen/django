from django.shortcuts import render

# Create your views here.
def example_view(request):
    # python manage.py migrate
    # check apps.py file inside my_app
    # confirm Config class is there
    # add Config to INSTALLED_APPS ('my_app.apps.MyAppConfig')
    # python manage.py makemigrations my_app (result is No changes detected in app 'my_app')
    # python manage.py migrate (no migrations to apply)
    # create my_app/templates/my_app/home.html
    return render(request,'my_app/home.html')

def variable_view(request):

    # MUST BE A DICTIONARY
    my_var = {'first_name':'Rosalind','last_name':'Franklin',
               'some_list':[1,2,3],'some_dict':{'inside_key':'inside_value'}}


    return render(request,'my_app/variable.html',context=my_var)