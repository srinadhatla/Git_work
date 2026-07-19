from django.db.models import Avg, Count
from django.utils import timezone

from employees.models import Employee, Department


def get_dashboard_statistics():
    today = timezone.now().date()
    return {
        "total_employees": Employee.objects.count(),
        "active_employees": Employee.objects.filter(is_active=True).count(),
        "inactive_employees": Employee.objects.filter(is_active=False).count(),
        "total_departments": Department.objects.count(),
        "joined_today": Employee.objects.filter(joining_date=today).count(),
        "average_salary": Employee.objects.aggregate(Avg("salary"))["salary__avg"],
        "department_count": Department.objects.annotate(employee_count=Count("employees")),}