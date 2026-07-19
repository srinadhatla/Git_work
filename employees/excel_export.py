import openpyxl
from openpyxl import Workbook

from io import BytesIO

from .models import Employee


def export_employees():
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Employees"

    headers = [
        "Employee ID",
        "First Name",
        "Last Name",
        "Email",
        "Phone",
        "Department",
        "Designation",
        "Salary",
        "Joining Date"
    ]

    sheet.append(headers)
    employees = Employee.objects.all()
    for employee in employees:
        sheet.append(
            [
                employee.employee_id,
                employee.first_name,
                employee.last_name,
                employee.email,
                employee.phone,
                employee.department.name
                if employee.department
                else "",

                employee.designation,
                employee.salary,
                employee.joining_date
            ]
        )


    output = BytesIO()
    workbook.save(output)
    output.seek(0)

    return output