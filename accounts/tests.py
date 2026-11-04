from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from .models import CustomUser

class AccountsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            username="student_user",
            email="student@campus.edu",
            password="SecurePassword123!",
            first_name="Jane",
            last_name="Doe",
            course="BS Information Technology",
            role=CustomUser.Role.STUDENT
        )

    def test_signup_creates_user_and_shows_success_message(self):
        signup_data = {
            "username": "newuser",
            "email": "newuser@campus.edu",
            "first_name": "John",
            "last_name": "Smith",
            "course": "BS Computer Science",
            "password1": "ComplexPass123!@",
            "password2": "ComplexPass123!@",
        }
        response = self.client.post(reverse("signup"), signup_data, follow=True)
        self.assertRedirects(response, reverse("login"))

        # Verify user created in DB
        new_user = CustomUser.objects.get(username="newuser")
        self.assertEqual(new_user.email, "newuser@campus.edu")
        self.assertEqual(new_user.course, "BS Computer Science")

        # Verify success message
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("Account created successfully" in str(m) for m in messages))

    def test_profile_edit_requires_login(self):
        response = self.client.get(reverse("profile_edit"))
        self.assertNotEqual(response.status_code, 200)
        self.assertIn(reverse("login"), response.url)

    def test_profile_edit_renders_with_current_user_data(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("profile_edit"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jane")
        self.assertContains(response, "Doe")
        self.assertContains(response, "BS Information Technology")

    def test_profile_edit_updates_user_and_shows_success_message(self):
        self.client.force_login(self.user)
        update_data = {
            "first_name": "Janet",
            "last_name": "Doe-Updated",
            "email": "janet.updated@campus.edu",
            "course": "BS Software Engineering",
        }
        response = self.client.post(reverse("profile_edit"), update_data, follow=True)
        self.assertRedirects(response, reverse("dashboard"))

        # Verify DB updated
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, "Janet")
        self.assertEqual(self.user.last_name, "Doe-Updated")
        self.assertEqual(self.user.email, "janet.updated@campus.edu")
        self.assertEqual(self.user.course, "BS Software Engineering")

        # Verify success message
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("profile has been updated successfully" in str(m) for m in messages))
