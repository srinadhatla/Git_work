from django.test import TestCase

from leave_management.permissions import (
    IsEmployee,
    IsManager,
    IsHR,
)


class PermissionTest(TestCase):
    def test_permission_classes_exist(self):
        self.assertIsNotNone(IsEmployee)
        self.assertIsNotNone(IsManager)
        self.assertIsNotNone(IsHR)