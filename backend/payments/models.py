# Create your models here.
from django.db import models
from users.models import User
from buses.models import Schedule

class Booking(models.Model):
    passenger = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'passenger'})
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()
    is_paid = models.BooleanField(default=False)
    qr_code = models.ImageField(upload_to='qrs/', blank=True, null=True)
    booked_at = models.DateTimeField(auto_now_add=True)
