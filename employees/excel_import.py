import openpyxl
from datetime import datetime

from .models import Employee, Department

def import_employees(file):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook.active
    total_rows = 0
    created = 0
    failed = 0
    errors = []

    for row in sheet.iter_rows(min_row=2,values_only=True):
        total_rows += 1
        try:
            (
                employee_id,
                first_name,
                last_name,
                email,
                phone,
                department,
                designation,
                salary,
                joining_date
            ) = row

            if not email:
                raise Exception("Email missing")

            if Employee.objects.filter(email=email).exists():
                raise Exception("Duplicate email")

            department_obj, created_dept = Department.objects.get_or_create(name=department)

            Employee.objects.create(
                employee_id=employee_id,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                department=department_obj,
                designation=designation,
                salary=salary,
                joining_date=joining_date
            )


            created += 1

        except Exception as e:
            failed += 1
            errors.append(
                {
                    "row": total_rows + 1,
                    "error": str(e)
                }
            )


    return {
        "total_rows": total_rows,
        "created": created,
        "failed": failed,
        "errors": errors
    }