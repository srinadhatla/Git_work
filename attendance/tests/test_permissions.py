from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()

class AttendancePermissionTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username="john",
            password="password123"
        ) 
        self.assertTrue(user.check_password("password123"))