from django.db.models import Sum, Count
from django.db.models.functions import ExtractMonth

from .models import LeaveBalance, LeaveRequest

def employee_leave_summary(employee, year):
    balances = LeaveBalance.objects.filter(employee=employee,year=year,)
    return {
        "employee": employee.employee_id,
        "year": year,
        "allocated": sum(balance.allocated_days for balance in balances),
        "used": sum(balance.used_days for balance in balances),
        "remaining": sum(balance.remaining_days for balance in balances),
    }

def department_leave_report():
    return (LeaveRequest.objects.values("employee__department__name").annotate(
            total_requests=Count("id"),
            total_leave_days=Sum("total_days"),
        )
        .order_by("employee__department__name")
    )

def monthly_leave_trends(year):
    return (LeaveRequest.objects.filter(
            start_date__year=year,
            status=LeaveRequest.Status.APPROVED,
        )
        .annotate(
            month=ExtractMonth("start_date")
        )
        .values("month")
        .annotate(total=Count("id"))
        .order_by("month")
    )

def monthly_leave_trends(year):
    return (LeaveRequest.objects.filter(
            start_date__year=year,
            status=LeaveRequest.Status.APPROVED,
        )
        .annotate(month=ExtractMonth("start_date"))
        .values("month")
        .annotate(total=Count("id"))
        .order_by("month")
    )

def most_used_leave_type():
    return (LeaveRequest.objects.values("leave_type__name")
        .annotate(total=Count("id"))
        .order_by("-total")
    )

def employees_with_zero_balance():
    return LeaveBalance.objects.filter(
        remaining_days=0
    ).select_related("employee","leave_type",)