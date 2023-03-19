from django.shortcuts import render

def my_custom_page_not_found_view(request, exception):
    return render(request, 'error_view.html', status=404)