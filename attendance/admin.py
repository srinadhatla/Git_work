from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)

class AttendanceAdmin(admin.ModelAdmin):
    list_display = (
        "employee",
        "attendance_date",
        "check_in_time",
        "check_out_time",
        "attendance_status",
    )
    search_fields = (
        "employee__employee_id",
        "employee_first_name",
    )
    list_filter = (
        "attendance_status",
        "attendance_date",
    )