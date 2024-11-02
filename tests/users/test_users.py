from django.contrib.auth import get_user_model
from django.test import TestCase


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
