from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from decimal import Decimal
from bookings.models import TravelOption, Booking

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="john", password="password123")

        self.travel = TravelOption.objects.create(
            type=TravelOption.TRAIN,
            source="Chennai",
            destination="Bangalore",
            departure_time=timezone.now(),
            price=Decimal("1500.00"),
            available_seats=5
        )

    def test_home_page(self):
        response = self.client.get(reverse("bookings:home"))
        self.assertEqual(response.status_code, 200)

    def test_register_view(self):
        # self.user.first_name = "John"
        # self.user.last_name = "Doe"
        # self.user.email = "john@example.com"
        # self.user.save()
        
        # self.client.login(usename='john',password= "password123")
        response = self.client.post(reverse("bookings:register"), {
            "username": "john_updated",
            "first_name": "John",
            "last_name": "Doe",
            "email": "john_updated@example.com",
            "password1": "StrongPass!123@",   # more complex password
            "password2": "StrongPass!123@"
        })
        if response.status_code == 200:
            print(response.context["form"].errors)
        # should redirect to login
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="john").exists())

    def test_travel_list_view(self):
        response = self.client.get(reverse("bookings:travel-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Chennai")

    def test_travel_list_with_filters(self):
        response = self.client.get(reverse("bookings:travel-list"), {"source": "Chennai"})
        self.assertContains(response, "Chennai")

    def test_profile_view_update(self):
        self.client.login(username="john", password="password123")
        response = self.client.post(reverse("bookings:profile"), {
            "username": "john_updated",
            "first_name": "John",
            "last_name": "Doe",
            "email":"john_updated@example.com",
            "phone_number": "1234567890",
            "address": "Earth"
        })
        # profile update redirects on success
        self.assertEqual(response.status_code, 302)

    def test_booking_create_success(self):
        self.client.login(username="john", password="password123")
        response = self.client.post(
            reverse("bookings:booking-create", args=[self.travel.id]),
            {"number_of_seats": 2}
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Booking.objects.filter(user=self.user).exists())

    def test_booking_create_more_than_available(self):
        self.client.login(username="john", password="password123")
        response = self.client.post(
            reverse("bookings:booking-create", args=[self.travel.id]),
            {"number_of_seats": 10}
        )
        self.assertEqual(response.status_code, 200)  # form re-rendered with error
        self.assertFalse(Booking.objects.filter(user=self.user).exists())

    def test_booking_list_view(self):
        Booking.objects.create(
            user=self.user,
            travel_option=self.travel,
            number_of_seats=1,
            total_price=Decimal("1500.00"),
            status=Booking.CONFIRMED
        )
        self.client.login(username="john", password="password123")
        response = self.client.get(reverse("bookings:booking-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Chennai")

    def test_booking_cancel(self):
        booking = Booking.objects.create(
            user=self.user,
            travel_option=self.travel,
            number_of_seats=1,
            total_price=Decimal("1500.00"),
            status=Booking.CONFIRMED
        )
        self.client.login(username="john", password="password123")
        response = self.client.post(reverse("bookings:booking-cancel", args=[booking.id]))
        booking.refresh_from_db()
        self.assertEqual(booking.status, Booking.CANCELLED)
