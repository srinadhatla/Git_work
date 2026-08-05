from django.contrib import admin
from .models import LeaveType, LeaveBalance, LeaveRequest

@admin.register(LeaveType)
class LeaveTypeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "annual_quota",
        "is_paid",
        "created_at",
    )
    search_fields = ("name", "code")
    list_filter = ("is_paid",)
    ordering = ("name",)

@admin.register(LeaveBalance)
class LeaveBalanceAdmin(admin.ModelAdmin):
    list_display = (
        "employee",
        "leave_type",
        "allocated_days",
        "used_days",
        "remaining_days",
        "year",
    )
    search_fields = (
        "employee__employee_id",
        "employee__first_name",
        "employee__last_name",
    )
    list_filter = (
        "leave_type",
        "year",
    )
    ordering = ("employee",)

@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = (
        "employee",
        "leave_type",
        "start_date",
        "end_date",
        "total_days",
        "status",
        "applied_at",
    )
    search_fields = (
        "employee__employee_id",
        "employee__first_name",
        "employee__last_name",
        "reason",
    )
    list_filter = (
        "status",
        "leave_type",
        "start_date",
    )
    ordering = ("-created_at",)