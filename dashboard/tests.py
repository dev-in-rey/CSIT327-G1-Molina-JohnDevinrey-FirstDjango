from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import CustomUser

class DashboardTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.student = CustomUser.objects.create_user(
            username="student_user",
            password="SecurePassword123!",
            role=CustomUser.Role.STUDENT,
            course="BSIT"
        )
        self.admin_user = CustomUser.objects.create_user(
            username="admin_user",
            password="SecurePassword123!",
            role=CustomUser.Role.ADMIN,
            course="BSCS"
        )

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse("dashboard"))
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('dashboard')}")

    def test_dashboard_renders_for_logged_in_user(self):
        self.client.force_login(self.student)
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "BSIT")
        self.assertContains(response, "Edit Profile")

    def test_student_cannot_access_admin_panel(self):
        self.client.force_login(self.student)
        response = self.client.get(reverse("admin_panel"))
        self.assertEqual(response.status_code, 403)

    def test_admin_can_access_admin_panel(self):
        self.client.force_login(self.admin_user)
        response = self.client.get(reverse("admin_panel"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Admin Panel")
