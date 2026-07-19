from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from employees.models import Employee, Department
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import date

User = get_user_model()

class EmployeeAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        self.department = Department.objects.create(name="IT")

        self.employee = Employee.objects.create(
            employee_id="EMP00001",
            first_name="sricastic",
            last_name="test",
            email="test@gmail.com",
            phone="9876543210",
            department=self.department,
            designation="Developer",
            salary=50000,
            joining_date=date.today(),
            is_active=True,
        )

    def test_get_employee_list(self):
        url = reverse("employee-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_employee(self):
        url = reverse("employee-list")
        data = {
            "employee_id": "EMP00002",
            "first_name": "Sanju",
            "last_name": "Samson",
            "email": "sanju@blackroth.in",
            "phone": "9876543222",
            "department": self.department.id,
            "designation": "Backend Developer",
            "salary": 70000,
            "joining_date": str(timezone.now().date()),
            "is_active": True
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 2)

    def test_get_employee_detail(self):
        url = reverse("employee-detail", args=[self.employee.id])

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["employee_id"], "EMP00001")

    def test_update_employee(self):
        url = reverse("employee-detail", args=[self.employee.id])

        data = {
            "employee_id": "EMP00001",
            "first_name": "Shreyas",
            "last_name": "Iyer",
            "email": "shreyas@blackroth.in",
            "phone": "9876543210",
            "department": self.department.id,
            "designation": "Senior Developer",
            "salary": 80000,
            "joining_date": str(timezone.now().date()),
            "is_active": True
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employee(self):
        url = reverse("employee-detail", args=[self.employee.id])

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_employee_data(self):
        url = reverse("employee-list")
        data = {
            "employee_id" : "",
            "first_name" : "",
            "email" : "invalid-email", 
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unauthorized_request(self):
        self.client.credentials()

        url = reverse("employee-list")

        response = self.client.get(url)
        self.assertIn(response.status_code, [status.HTTP_403_FORBIDDEN, status.HTTP_401_UNAUTHORIZED])

def test_employee_api_without_token(self):
    self.client.credentials()

    url = "/api/v1/employees/"
    response = self.client.get(url)

    self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_employee_api_with_token(self):

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
        )
        url = "/api/v1/employees/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AuthenticationAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123"
        )

    def test_login_success(self):
        url = "/api/v1/auth/login/"
        data = {
            "username" : "testuser",
            "password" : "testpassword123"
        }
        response = self.client.post(
            url,
            data,
            format="json"
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_invalid_login(self):
        url = "/api/v1/auth/login/"

        data = {
            "username" : "testuser",
            "password" : "wrongpassword",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_missing_fields(self):
        url = "/api/v1/auth/login/"
        data = {
            "username" : "testuser",
        }
        response = self.client.post(url,data,format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class JWTAuthenticationTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(   
            username="jwtuser",
            email="test@blackroth.in",
            password="password123",
        )
        refresh = RefreshToken.for_user(self.user)

        self.refresh_token = str(refresh)
        self.access_token = str(refresh.access_token)

    def test_refresh_token_success(self):
        url = "/api/v1/auth/refresh/"

        data = {
            "refresh" : self.refresh_token
        }
        response = self.client.post(
            url,
            data,
            format="json"
        )
        print("Status Code:", response.status_code)
        print("Response:", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_invalid_refresh_token(self):
        url = "/api/v1/auth/refresh/"

        data = {
            "refresh" : "invalid_token"
        }
        response = self.client.post(
            url,
            data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_missing_refresh_token(self):
        url = "/api/v1/auth/refresh/"

        data = {}
        response = self.client.post(
            url,
            data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_logout(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        url = "/api/v1/auth/logout/"
        data = {
            "refresh" : self.refresh_token
        }
        response = self.client.post(
            url,
            data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_change_password_success(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        url = "/api/v1/auth/change-password/"
        data = {
            "old_password" : "password123",
            "new_password" : 'newpassword123'
        }
        response = self.client.post(
            url,
            data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password("newpassword123"))

    def test_change_password_wrong_old_password(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        url = "/api/v1/auth/change-password/"
        data = {
            "old_password" : "wrongpassword",
            "new_password" : "newpassword123"
        }
        response = self.client.post(
            url,
            data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_forgot_password(self):
        url = "/api/v1/auth/forgot-password/"

        data = {
            "email" : self.user.email
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_expired_token(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer invalid_or_expired_token")

        response = self.client.get("/api/v1/api/employees/")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

