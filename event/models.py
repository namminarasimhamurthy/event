from django.db import models

class UserRegistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)

class EventBooking(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    event_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    event_date = models.DateField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.email
