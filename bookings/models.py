from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15,blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class TravelOption(models.Model):
    
    FLIGHT = 'FL'
    TRAIN = 'TR'
    BUS = 'BS'

    TRAVEL_TYPES = [
        (FLIGHT, 'Flight'),
        (TRAIN, 'Train'),
        (BUS, 'Bus'),
    ]

    type = models.CharField(max_length=2,choices=TRAVEL_TYPES,default=FLIGHT)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    available_seats = models.IntegerField()

    def __str__(self):
        return f'{self.get_type_display()}:{self.source} to {self.destination} on {self.departure_time}'
    
    class Meta:
        ordering = ['departure_time']

class Booking(models.Model):

    CONFIRMED = 'CF'
    CANCELLED = 'CL'

    STATUS_TYPES = [
        (CONFIRMED,'Confirmed'),
        (CANCELLED,'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    travel_option = models.ForeignKey(TravelOption, on_delete=models.CASCADE)
    number_of_seats = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add = True)
    status = models.CharField(
        max_length=2,
        choices=STATUS_TYPES,
        default=CONFIRMED,
    )

    def __str__(self, *args, **kwargs):

        self.total_price = self.travel_option.price * self.number_of_seats
        super().save(*args,**kwargs)
        


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender = User)
def save_user_prefile(sender, instance, **kwargs):
    instance.profile.save()
