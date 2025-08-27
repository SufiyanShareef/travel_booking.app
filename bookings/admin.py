from django.contrib import admin
from .models import Profile, TravelOption, Booking

# Register your models here.
admin.site.register(Profile)
admin.site.register(TravelOption)
admin.site.register(Booking)