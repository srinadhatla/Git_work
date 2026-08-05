from datetime import date
from decimal import Decimal
from django.test import TestCase
from attendance.services.attendance_service import AttendanceService
from departments.models import Department
from employees.models import Employee

class AttendanceServiceTest(TestCase):
    def setUp(self):
        department = Department.objects.create(
            name="Engineering",
            code="ENG001"
        )

        self.employee = Employee.objects.create(
            employee_id="EMP001",
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            dob="2003-06-12",
            phone="9999999999",
            department=department,
            designation="Developer",
            salary=60000,
            joining_date=date.today(),
            status="Active",
        )

    def test_check_in(self):
        print("Employee status:", self.employee.status)
        attendance = AttendanceService.check_in(self.employee)
        self.assertIsNotNone(attendance.check_in_time)
        

    def test_calculate_overtime(self):
        overtime = AttendanceService.calculate_overtime(Decimal("9.50"))
        self.assertEqual(overtime,Decimal("1.50"))