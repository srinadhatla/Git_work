from django.utils import timezone
from django.core.exceptions import ValidationError

from .models import LeaveRequest

def validate_leave_dates(start_date, end_date, user=None):
    today = timezone.localdate()
    is_hr_override = False
    if user and user.is_staff:
        is_hr_override = True

    elif (user and hasattr(user, "employee") and user.employee.department.name.lower() == "hr"):
        is_hr_override = True

    if start_date < today and not is_hr_override:
        raise ValidationError("Leave cannot start in the past.")

    if end_date < start_date:
        raise ValidationError("End date cannot be before start date.")

def validate_overlap(employee, start_date, end_date):
    overlap = LeaveRequest.objects.filter(
        employee=employee,
        start_date__lte=end_date,
        end_date__gte=start_date,
        status__in=[
            LeaveRequest.Status.PENDING,
            LeaveRequest.Status.MANAGER_APPROVED,
            LeaveRequest.Status.APPROVED,
        ],
    ).exists()

    if overlap:
        raise ValidationError("Overlapping leave request found.")

def validate_leave_balance(balance, total_days):
    if balance.remaining_days < total_days:
        raise ValidationError("Insufficient leave balance.")

def validate_approved_leave(leave_request):
    if leave_request.status == LeaveRequest.Status.APPROVED:
        raise ValidationError("Approved leave cannot be modified.")