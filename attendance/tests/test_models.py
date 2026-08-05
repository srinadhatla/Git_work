from datetime import date
from decimal import Decimal
from django.test import TestCase
from attendance.models import Attendance
from departments.models import Department
from employees.models import Employee

class AttendanceModelTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name="Engineering",code="ENG001")
        self.employee = Employee.objects.create(
            employee_id="EMP001",
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            dob="2002-07-15",
            phone="9876543210",
            department=self.department,
            designation="Developer",
            salary=50000,
            joining_date=date.today(),
        )

    def test_create_attendance(self):
        attendance = Attendance.objects.create(
            employee=self.employee,
            attendance_date=date.today(),
            attendance_status=Attendance.AttendanceStatus.PRESENT,
            working_hours=Decimal("8.00")
        )
        self.assertEqual(attendance.employee.employee_id,"EMP001")
        self.assertEqual(attendance.attendance_status,Attendance.AttendanceStatus.PRESENT)

    def test_string_representation(self):
        attendance = Attendance.objects.create(employee=self.employee,attendance_date=date.today())
        self.assertIn("EMP001",str(attendance))