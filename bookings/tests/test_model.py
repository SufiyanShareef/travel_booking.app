from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Profile, TravelOption, Booking
from django.utils import timezone
from decimal import Decimal


class ProfileModelTest(TestCase):
    def test_profile_created_on_user_creation(self):
        user = User.objects.create_user(username="john", password="password123")
        self.assertTrue(hasattr(user, "profile"))
        self.assertIsInstance(user.profile, Profile)

    def test_profile_fields(self):
        user = User.objects.create_user(username="alice", password="password123")
        user.profile.phone_number = "1234567890"
        user.profile.address = "Somewhere on Earth"
        user.profile.save()
        profile = Profile.objects.get(user=user)
        self.assertEqual(profile.phone_number, "1234567890")
        self.assertEqual(profile.address, "Somewhere on Earth")


class TravelOptionModelTest(TestCase):
    def test_create_travel_option(self):
        travel = TravelOption.objects.create(
            type=TravelOption.FLIGHT,
            source="Hyderabad",
            destination="Delhi",
            departure_time=timezone.now(),
            price=Decimal("2500.00"),
            available_seats=50
        )
        self.assertEqual(travel.type, TravelOption.FLIGHT)
        self.assertEqual(travel.available_seats, 50)
        self.assertIn("Hyderabad", str(travel))


class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="john", password="password123")
        self.travel = TravelOption.objects.create(
            type=TravelOption.BUS,
            source="Mumbai",
            destination="Pune",
            departure_time=timezone.now(),
            price=Decimal("500.00"),
            available_seats=40
        )

    def test_create_booking_and_total_price(self):
        booking = Booking.objects.create(
            user=self.user,
            travel_option=self.travel,
            number_of_seats=2,
            total_price=Decimal("0.00"),  # will be recalculated in save/str
            status=Booking.CONFIRMED
        )
        # Check recalculation of price
        self.assertEqual(booking.total_price, Decimal("1000.00"))
        self.assertEqual(booking.status, Booking.CONFIRMED)

    def test_booking_status_cancelled(self):
        booking = Booking.objects.create(
            user=self.user,
            travel_option=self.travel,
            number_of_seats=1,
            total_price=Decimal("500.00"),
            status=Booking.CANCELLED
        )
        self.assertEqual(booking.status, Booking.CANCELLED)
