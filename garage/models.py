from django.db import models


class Booking(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    vehicle_registration = models.CharField(max_length=20)
    booking_date = models.DateField()
    service_required = models.CharField(max_length=100)
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.vehicle_registration}"