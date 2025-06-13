# admin.py
from django.contrib import admin
from .models import UserRegistration
from .models import EventBooking 

class userRegistrationAdmin(admin.ModelAdmin):
    list_display = ("name","email","confirm_password","password")
admin.site.register(UserRegistration,userRegistrationAdmin)

class EventBookingAdmin(admin.ModelAdmin):
    list_display = ("full_name","email","event_name","mobile_number","event_date","amount","description")
admin.site.register(EventBooking,EventBookingAdmin)