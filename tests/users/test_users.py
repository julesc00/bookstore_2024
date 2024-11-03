from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from users.forms import CustomUserCreationForm
from users.views import SignupPageView


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="Jemima",
            email="jemima.eloise@bonita.com",
            password="jemi123"
        )
        self.assertEqual(user.username, "Jemima")
        self.assertEqual(user.email, "jemima.eloise@bonita.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="superadmin",
            email="superadmin@somewhere.com",
            password="pass123"
        )

        self.assertEqual(admin_user.username, "superadmin")
        self.assertEqual(admin_user.email, "superadmin@somewhere.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTests(TestCase):
    def setUp(self):
        url = reverse("users:signup")
        self.res = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.res.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(self.res, "users/signup.html")
        self.assertContains(self.res, "Sign Up")
        self.assertNotContains(self.res, "Hi there you.")

    def test_signup_form(self):
        form = self.res.context.get("form")
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.res, "csrfmiddlewaretoken")

    # Test not passing, come back to it
    def test_signup_view(self):
        view = resolve("accounts/users/signup/")
        self.assertEqual(
            view.func.__name__,
            SignupPageView.as_view().__name__
        )
