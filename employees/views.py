from django.shortcuts import render
from django.db.models import Count, Max, Min, Avg

from django.utils import timezone

from employees.models import Employee, Department

def dashboard(request):
    today = timezone.now().date()
    
    context = {
        "total_employees": Employee.objects.count(),
        "active_employees": Employee.objects.filter(is_active=True).count(),
        "inactive_emmployees": Employee.objects.filter(is_active=False).count(),
        "total_departments": Employee.objects.count(),
        "joined_today": Employee.objects.filter(joining_date=today).count(),
        "joined_this_month": Employee.objects.filter(joining_date__month=today.month,joining_date__year=today.year).count(),
        "salary_stats": Employee.objects.aggregate(highest_salary=Max("salary"),lowest_salary=Min("salary"),average_salary=Avg("salary")),
        "department_employee_count": Department.objects.annotate(employee_count=Count("employee")),
    }
    return render(request, "dashboard.html",context)