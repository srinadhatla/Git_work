from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class AttendanceAPITest(APITestCase):
    def setUp(self):
        self.url = reverse("attendance-check-in")

    def test_authentication_required(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)