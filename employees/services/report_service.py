from employees.models import Employee, Department


def get_employee_summary():

    return {
        "total": Employee.objects.count(),
        "active": Employee.objects.filter(is_active=True).count(),
        "inactive": Employee.objects.filter(is_active=False).count(),
    }


def get_department_summary():

    return {"departments": Department.objects.count(),}