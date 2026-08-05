from datetime import date
from django.test import TestCase
from employees.models import Employee
from leave_management.models import (
    LeaveType,
    LeaveBalance,
    LeaveRequest,
)
from departments.models import Department

class LeaveBalanceModelTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name="IT")
        self.employee = Employee.objects.create(
            employee_id="EMP00001",
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            phone="9999999999",
            dob=date(1998,5,15),
            department=self.department,
            designation="Developer",
            salary=50000,
            joining_date=date(2026,1,1),
            status="Active",
            gender="Male",
        )

        self.leave_type = LeaveType.objects.create(
            name="Sick Leave",
            code="SL",
            annual_quota=10,
            is_paid=True,
        )
    def test_leave_balance_creation(self):
        balance = LeaveBalance.objects.create(
            employee=self.employee,
            leave_type=self.leave_type,
            allocated_days=10,
            used_days=2,
            remaining_days=8,
            year=2026,
        )
        self.assertEqual(balance.remaining_days,8,)

class LeaveRequestModelTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name="Testing")
        self.employee = Employee.objects.create(
            employee_id="EMP00002",
            first_name="Jane",
            last_name="Doe",
            email="jane@example.com",
            phone="8888888888",
            dob=date(1998,5,15),
            department=self.department,
            designation="Tester",
            salary=40000,
            joining_date=date(2026,1,1),
            status="Active",
            gender="Male",
        )

        self.leave_type = LeaveType.objects.create(
            name="Earned Leave",
            code="EL",
            annual_quota=15,
            is_paid=True,
        )

    def test_leave_request_creation(self):
        leave = LeaveRequest.objects.create(
            employee=self.employee,
            leave_type=self.leave_type,
            start_date=date(2026, 8, 10),
            end_date=date(2026, 8, 12),
            total_days=3,
            reason="Vacation",
        )

        self.assertEqual(leave.status,LeaveRequest.Status.PENDING_MANAGER)