from django.test import TestCase
from django.db import IntegrityError
from django.utils import timezone

from employees.models import Employee, Department
from django.core.exceptions import ValidationError

from datetime import date, timedelta

from decimal import Decimal

class DepartmentModelTest(TestCase):

    def setUp(self):
        self.department = Department.objects.create(name="IT",description="Information Technology")

    def test_department_creation(self):
        self.assertEqual(self.department.name, "IT")
        self.assertEqual(self.department.description, "Information Technology")

    def test_duplicate_department_name(self):
        with self.assertRaises(IntegrityError):
            Department.objects.create(name="IT", description="Duplicate Department")

class EmployeeModelTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name="HR", description = "Human Resources")
        self.employee = Employee.objects.create(
            employee_id="EMP0001",
            first_name="sricastic",
            last_name="atla",
            email="sricastic@blackroth.in",
            phone="9298482428",
            department=self.department,
            designation="Python Developer",
            salary="30000",
            joining_date=timezone.now().date(),
            is_active=True,
        )

    def test_employee_creation(self):
        self.assertEqual(self.employee.employee_id, "EMP0001")
        self.assertEqual(self.employee.first_name, "sricastic")
        self.assertEqual(self.employee.email, "sricastic@blackroth.in")
        self.assertEqual(self.employee.salary, Decimal("30000"))

    def test_unique_employee_id(self):
            Employee.objects.create(
                employee_id="EMP00001",
                first_name="Alex",
                last_name="Smith",
                email="alex@blackroth.in",
                phone="9876543211",
                department=self.department,
                designation="Developer",
                salary=40000,
                joining_date=timezone.now().date(),
                is_active=True
            )

    def test_unique_email(self):
        with self.assertRaises(ValidationError):
            Employee.objects.create(
                employee_id="EMP00001",
                first_name="Alex",
                last_name="Smith",
                email="sricastic@blackroth.in",
                phone="9876543211",
                department=self.department,
                designation="Developer",
                salary=40000,
                joining_date=timezone.now().date(),
                is_active=True
            )

    def test_salary_validation(self):
        employee = Employee(
            employee_id="EMP00003",
            first_name="josh",
            last_name="buttler",
            email="josh@blackroth.in",
            phone="9876543213",
            department=self.department,
            designation="Tester",
            salary=-5000,
            joining_date=timezone.now().date()
        )
        with self.assertRaises(ValidationError):
            employee.full_clean()

    def test_joining_date_validation(self):
        future_date = date.today() + timedelta(days=10)
        employee = Employee(
            
            employee_id="EMP00004",
            first_name="virat",
            last_name="kohli",
            email="virat@blackroth.in",
            phone="9876543214",
            department=self.department,
            designation="Developer",
            salary=50000,
            joining_date=future_date
        )
        with self.assertRaises(ValidationError):
            employee.full_clean()
    def test_create_employee(self):
        employee = Employee.objects.create(
            employee_id="EMP00005",
            first_name="Rohith",
            last_name="Sharma",
            email="rohith@blackroth.in",
            phone="9876543220",
            department=self.department,
            designation="Software Engineer",
            salary=60000,
            joining_date=timezone.now().date(),
            is_active=True
        )

        self.assertEqual(Employee.objects.count(), 2)
        self.assertEqual(employee.first_name, "Rohith")
        self.assertEqual(employee.department.name, "HR")

    def test_update_employee(self):
            self.employee.first_name = "Dhoni"
            self.employee.salary = 75000
            self.employee.save()

            updated_employee = Employee.objects.get(id=self.employee.id)
            self.assertEqual(updated_employee.first_name, "Dhoni")
            self.assertEqual(updated_employee.salary, 75000)

    def test_delete_employee(self):
        self.employee.delete()

        self.assertEqual(Employee.objects.count(), 0)

    def test_search_employee(self):
        employee = Employee.objects.filter(first_name="sricastic")

        self.assertEqual(employee.count(), 1)
        self.assertEqual(employee.first().email, "sricastic@blackroth.in")

    def test_filter_employee_by_department(self):
        employees = Employee.objects.filter(department=self.department)

        self.assertEqual(employees.count(), 1)

    def test_employee_department_relationship(self):
        self.assertEqual(self.employee.department.name, "HR")
        self.assertEqual(self.employee.department.description, "Human Resources")

    def test_employee_department_relationship(self):
        employees = self.department.employees.all()

        self.assertEqual(employees.count(), 1)
        self.assertEqual(employees.first().first_name, "sricastic")

    def test_department_employee_relationship(self):
        employees = self.department.employees.all()

        self.assertEqual(employees.count(), 1)

class FixtureText(TestCase):
    fixtures = [
        "user.json",
        "employees.json",
        "departments.json"
    ]
    from django.test import TestCase


class FixtureTest(TestCase):

    fixtures = [
        "users.json",
        "departments.json",
        "employees.json"
    ]


    def test_employee_fixture_loaded(self):
        from employees.models import Employee
        employee = Employee.objects.get(employee_id="EMP00001")

        self.assertEqual(employee.first_name,"Employee1")