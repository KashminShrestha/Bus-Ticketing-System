# Create your models here.
from django.db import models
from users.models import User

class Route(models.Model):
    start_point = models.CharField(max_length=100)
    end_point = models.CharField(max_length=100)
    duration = models.DurationField()

    def __str__(self):
        return f"{self.start_point} → {self.end_point}"

class Bus(models.Model):
    number_plate = models.CharField(max_length=20, unique=True)
    capacity = models.PositiveIntegerField()
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'driver'})

class Schedule(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
