from django.db import models
from django.utils import timezone

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    departure = models.ForeignKey("City", on_delete=models.CASCADE, related_name="flights_from", null=True)
    destination = models.ForeignKey(City, on_delete=models.CASCADE, related_name="flights_to", null=True)
    departure_at = models.DateTimeField()
    min_price_usd = models.FloatField()
    transfers = models.BooleanField(default=False)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.flight_number





