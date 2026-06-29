from employees.repositories.employee_repository import EmployeeRepository

from django.db import transaction
from employees.models import Employee
from payroll.models import Payroll
from audit.models import AuditLog

class EmployeeService:

    @staticmethod
    def get_all_employees():
        return EmployeeRepository.get_all()

    @staticmethod
    def get_employee(employee_id):
        return EmployeeRepository.get_by_id(employee_id)

    @staticmethod
    def create_employee(data):
        return EmployeeRepository.create(data)

    @staticmethod
    def update_employee(employee_id, data):

        employee = EmployeeRepository.get_by_id(employee_id)

        return EmployeeRepository.update(employee,data)

    @staticmethod
    def delete_employee(employee_id):

        employee = EmployeeRepository.get_by_id(employee_id)

        EmployeeRepository.delete(employee)
        

class SalaryService:
    @staticmethod
    def process_salary(employee_id, increment_amount, user=None):
        with transaction.atomic():
            employee = Employee.objects.select_for_update().get(id=employee_id)
            old_salary = employee.salary
            employee.salary += increment_amount
            employee.save()
            Payroll.objects.create(
                employee=employee,
                basic_salary=old_salary,
                bonus=increment_amount,
                deductions=0,
                net_salary=employee.salary
            )

            AuditLog.objects.create(
                action="SALARY_UPDATE",
                employee=employee,
                old_value=old_salary,
                new_value=employee.salary,
                performed_by=user
            )
