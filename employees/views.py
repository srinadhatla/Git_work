from django.shortcuts import render
from django.db.models import Count, Max, Min, Avg

from django.utils import timezone

from employees.models import Employee, Department

from django.core.cache import cache

today = timezone.now().date()

from django.core.paginator import Paginator

from django.db.models import Q

from employees.services.dashboard_service import get_dashboard_statistics

from django.core.cache import cache

from employees.services.employee_service import (get_paginated_employees,search_employees,)

from employees.services.dashboard_service import (get_dashboard_statistics,)

def dashboard(request):
    dashboard_data = cache.get("dashboard_data")
    if not dashboard_data:
        dashboard_data = get_dashboard_statistics()
        cache.set("dashboard_data",dashboard_data,timeout=120,)
    return render(request, "dashboard.html", dashboard_data)


def employee_list(request):
    employees = cache.get("employees_list")

    if employees is None:
        employees = list(
            Employee.objects.select_related("department").only(
                "id",
                "employee_id",
                "first_name",
                "last_name",
                "department__name",
                "salary",
            )
        )
        cache.set("employees_list", employees, timeout=300)

    paginator = Paginator(employees, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "employees/employees_list.html", {"page_obj": page_obj})

def employee_search(request):
    query = request.GET.get("q", "")
    department = request.GET.get("department", "")
    status = request.GET.get("status", "")
    employees = search_employees(query,department,status,)
    return render(request,"employees/employee_search.html",
        {
            "employees": employees,
            "query": query,
            "department": department,
            "status": status,
        },
    )
    
def department_list(request):
    departments = cache.get("departments")
    if departments is None:
        departments = Department.objects.prefetch_related("employee_set")
        cache.set("departments", departments, timeout=1800)

    paginator = Paginator(departments, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "employees/departments_list.html", {"page_obj": page_obj})
            