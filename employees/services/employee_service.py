from django.core.paginator import Paginator
from django.db.models import Q

from employees.models import Employee


def get_paginated_employees(page_number):

    employees = (Employee.objects.select_related("department").all())
    paginator = Paginator(employees, 20)
    return paginator.get_page(page_number)


def search_employees(query, department, status):
    employees = Employee.objects.select_related("department").all()
    if query:
        employees = employees.filter(
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(employee_id__icontains=query)
            | Q(email__icontains=query)
        )

    if department:
        employees = employees.filter(department__name__icontains=department)

    if status == "active":
        employees = employees.filter(is_active=True)

    elif status == "inactive":
        employees = employees.filter(is_active=False)

    return employees