from django.db import models
from django.utils import timezone

class Vehicle(models.Model):
    id = models.BigIntegerField(primary_key=True)
    plate = models.CharField(max_length=50)

class NavigationRecord(models.Model):
    id = models.BigIntegerField(primary_key=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)
    latitude = models.FloatField()
    longtitude = models.FloatField()
