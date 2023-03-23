from django.shortcuts import render, redirect
from django.urls import reverse
from . import models

# Create your views here.
def list(request):
    all_cars = models.Car.objects.all()
    context = {"all_cars": all_cars}
    return render(request, "cars/list.html", context=context)


def add(request):
    if request.POST:
        brand = request.POST.get("brand")
        year = int(request.POST.get("year"))
        color = request.POST.get("color")

        models.Car.objects.create(brand=brand, year=year, color=color)
        # if user submitted new car ---> list.html
        return redirect(reverse("cars:list"))
    else:
        return render(request, "cars/add.html")


def delete(request):
    if request.POST:
        # delete the car
        pk = request.POST.get("pk")
        try:
            models.Car.objects.get(pk=pk).delete()
            return redirect(reverse("cars:list"))
        except:
            print("pk not found")
            return redirect(reverse("cars:list"))
    else:
        return render(request, "cars/delete.html")
