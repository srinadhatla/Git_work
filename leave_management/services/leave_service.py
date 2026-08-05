from datetime import timedelta
from django.db import transaction
from django.utils import timezone
from django.core.exceptions import ValidationError

from leave_management.models import LeaveRequest,LeaveBalance
from leave_management import reports
from leave_management.notification_service import LeaveNotificationService
from leave_management.utils import log_leave_action, calculate_working_days
from leave_management.validators import validate_leave_dates

class LeaveService:
    @staticmethod
    def calculate_leave_days(start_date,end_date):
        return calculate_working_days(start_date,end_date)

    @staticmethod
    @transaction.atomic
    def apply_leave(employee, user, leave_type, start_date, end_date, reason):
        validate_leave_dates(start_date,end_date,user=user)
        total_days = LeaveService.calculate_leave_days(start_date, end_date)
        balance =  LeaveBalance.objects.filter(employee=employee,leave_type=leave_type,year=start_date.year).first()

        if not balance:
            raise ValidationError("Leave Balance not available")

        if balance.remaining_days<total_days:
            raise ValidationError("Insufficient leave balance")

        LeaveNotificationService.leave_applied(leave_request)
        log_leave_action(employee.user,"Leave Applied",leave_request,)

        overlapping = LeaveRequest.objects.filter(
            employee = employee,
            start_date__lte=end_date,
            end_date__gte=start_date,
            status__in=[
                LeaveRequest.Status.PENDING,
                LeaveRequest.Status.MANAGER_APPROVED,
                LeaveRequest.Status.APPROVED,
            ]
        ).exists()

        if overlapping:
            raise ValidationError("you have already leave during this period")

        leave_request = LeaveRequest.objects.create(
            employee=employee,
            leave_type=leave_type,
            start_date=start_date,
            end_date=end_date,
            total_days=total_days,
            reason=reason,
        )
        LeaveNotificationService.send_leave_applied_notification(leave_request)
        return leave_request

    @staticmethod
    @transaction.atomic
    def approve_leave(leave_request, approver_type="manager"):
        if approver_type == "manager":
            LeaveNotificationService.manager_approved(leave_request)
            
            log_leave_action(leave_request.employee.user,"Manager Approved",leave_request,)

        elif approver_type == "hr":
            leave_request.status = (LeaveRequest.Status.APPROVED)
            leave_request.approved_at = timezone.now()
            LeaveService.update_leave_balance(leave_request)
        leave_request.save()
        return leave_request

    @staticmethod
    def reject_leave(leave_request, comment=None):
        leave_request.status = (LeaveRequest.Status.REJECTED)
        leave_request.manager_comments = comment
        leave_request.save()
        return leave_request

    @staticmethod
    @transaction.atomic
    def cancel_leave(leave_request):
        if leave_request.status != LeaveRequest.Status.APPROVED:
            raise ValidationError("Only approved leave can be cancelled.")

        balance = LeaveBalance.objects.get(
            employee=leave_request.employee,
            leave_type=leave_request.leave_type,
            year=leave_request.start_date.year
        )
        LeaveNotificationService.leave_cancelled(leave_request)
        log_leave_action(leave_request.employee.user,"Leave Cancelled",leave_request,)

        balance.used_days -= leave_request.total_days
        balance.remaining_days += leave_request.total_days
        balance.save()

        leave_request.status = (LeaveRequest.Status.CANCELLED)
        leave_request.save()
        return leave_request

    @staticmethod
    def update_leave_balance(leave_request):
        balance = LeaveBalance.objects.get(
            employee=leave_request.employee,
            leave_type=leave_request.leave_type,
            year=leave_request.start_date.year
        )
        balance.used_days += (leave_request.total_days)
        balance.remaining_days -= (leave_request.total_days)
        balance.save()

    @staticmethod
    def employee_leave_summary(employee, year):
        balances = LeaveBalance.objects.filter(
            employee=employee,
            year=year
        )

        total_allocated = sum(b.allocated_days for b in balances)
        total_used = sum(b.used_days for b in balances)
        total_remaining = sum(b.remaining_days for b in balances)

        return {
            "year": year,
            "allocated": total_allocated,
            "used": total_used,
            "remaining": total_remaining
        }


    @staticmethod
    def company_leave_analytics(year):

        return {"monthly_trends":list(reports.monthly_leave_trends(year)),
            "department_report":list(reports.department_leave_report()),
            "most_used_leave_type":list(reports.most_used_leave_type()),
            "zero_leave_balance":reports.employees_with_zero_balance().count(),
            }