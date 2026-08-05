from rest_framework.test import APITestCase
from rest_framework import status

class LeaveAPITest(APITestCase):
    def test_login_required(self):
        response = self.client.get("/api/v1/leaves/")
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED,)