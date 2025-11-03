from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from flights.models import Flight, City


# Create your views here.
def greeting(request):
    context = {"flights": Flight.objects.all()}
    return render(request,
                  "flights/home.html",
                  context=context)

def cities_list(request):
    context = {"cities": City.objects.all()}
    return render(request, "flights/cities.html", context=context)

def flights_from_city(request, city_id):
    city = get_object_or_404(City, id=city_id)
    flights = city.flights_from.all()
    context = {"city": city, "flights": flights}

    return render(request, "flights/flights_from_city.html", context=context)