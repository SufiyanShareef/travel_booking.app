from django.test import TestCase
from django.contrib.auth.models import User
from bookings.forms import UserRegisterForm, UseeUpdateForm, ProfileUpdateForm


class UserRegisterFormTest(TestCase):
    def test_valid_register_form(self):
        form_data = {
            "username": "alice",
            "first_name": "Alice",
            "last_name": "Wonder",
            "email": "alice@example.com",
            "password1": "strongpassword123",
            "password2": "strongpassword123"
        }
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_register_form_password_mismatch(self):
        form_data = {
            "username": "bob",
            "first_name": "Bob",
            "last_name": "Builder",
            "email": "bob@example.com",
            "password1": "password123",
            "password2": "different123"
        }
        form = UserRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)


class UseeUpdateFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="john", password="password123", email="john@example.com"
        )

    def test_valid_update_form(self):
        form_data = {
            "username": "john_updated",
            "first_name": "John",
            "last_name": "Doe",
            "email": "newjohn@example.com"
        }
        form = UseeUpdateForm(data=form_data, instance=self.user)
        self.assertTrue(form.is_valid())

    def test_invalid_update_form_missing_email(self):
        form_data = {
            "username": "john_updated",
            "first_name": "John",
            "last_name": "Doe",
            "email": ""  # required field missing
        }
        form = UseeUpdateForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)


class ProfileUpdateFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="jane", password="password123")
        self.profile = self.user.profile

    def test_valid_profile_update(self):
        form_data = {
            "phone_number": "1234567890",
            "address": "Test address"
        }
        form = ProfileUpdateForm(data=form_data, instance=self.profile)
        self.assertTrue(form.is_valid())

    def test_profile_update_missing_address(self):
        form_data = {
            "phone_number": "1234567890",
            "address": ""
        }
        form = ProfileUpdateForm(data=form_data, instance=self.profile)
        self.assertTrue(form.is_valid())  # address is not required
