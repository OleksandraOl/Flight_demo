"""
URL configuration for Flight_demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from flights.views import greeting, cities_list, flights_from_city

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', greeting, name='flights'),
    path('cities/', cities_list, name='cities'),
    path('cities/<int:city_id>/', flights_from_city, name='flights_from_city'),
]
