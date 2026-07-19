from django.contrib.auth.models import User, Group
from django.test import TestCase
from rest_framework.test import APITestCase, APIClient

from employees.models import Employee, Department

from employees.permissions import IsHRorAdmin
from rest_framework.test import APIRequestFactory

class permissionTest(APITestCase):
    def setUp(self):

        self.department = Department.objects.create(
            name="IT",
            description="Information Technology"
        )
        self.hr_group, _=Group.objects.get_or_create(
            name="HR"
        )
        self.admin = User.objects.create_user(
            username="admin",
            password="admin123",
            is_staff=True
        )
        self.hr=User.objects.create_user(
            username="hr",
            password="hr123 "
        )
        self.hr.groups.add(self.hr_group)
        self.employee = User.objects.create_user(
            username="employee",
            password="emp123"
        )

    def test_admin_access(self):
        self.client.force_authenticate(
            user=self.admin
        )

        response = self.client.get(
            "/api/v1/employees/"
        )
        self.assertNotEqual(response.status_code, 401)

    def test_hr_access(self):

        self.client.force_authenticate(user=self.hr)

        response = self.client.get("/api/v1/api/employees/")

        self.assertNotEqual(response.status_code,401)

    def test_anonymous_access(self):

        response = self.client.get("/api/v1/api/employees/")
        self.assertEqual(response.status_code,401)

    def test_employee_cannot_upload_document(self):

        self.client.force_authenticate(user=self.employee)

        response = self.client.post("/api/v1/documents/upload/")

        self.assertEqual(response.status_code,403)

    def test_hr_can_upload_document(self):
        self.client.force_authenticate(user=self.hr)
        response = self.client.post("/documents/upload/")

        self.assertNotEqual(response.status_code, 403)

    def test_admin_can_upload_document(self):
        self.client.force_authenticate(user=self.admin)

        response = self.client.post("/documents/upload/")
        self.assertNotEqual(response.status_code, 403)

    def test_permission_class(self):

        factory = APIRequestFactory()
        request = factory.get("/")
        request.user = self.admin
        permission = IsHRorAdmin()

        self.assertTrue(permission.has_permission(request,None))