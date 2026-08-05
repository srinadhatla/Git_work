from datetime import date
from django.test import TestCase
from leave_management.services.leave_service import LeaveService

class LeaveServiceTest(TestCase):
    def test_calculate_leave_days(self):
        days = LeaveService.calculate_leave_days(
            date(2026, 8, 10),
            date(2026, 8, 12),
        )

        self.assertEqual(days,3,)