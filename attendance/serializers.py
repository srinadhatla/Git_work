from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    employee_id = serializers.CharField(source="employee_id,read_only=true")
    employee_name = serializers.SerializerMethodField()
    department = serializers.CharField(source="employee.department.name",read_only=True)

    class Meta:
        model = Attendance
        fields = [
            "id",
            "employee",
            "employee_id",
            "employee_name",
            "department",
            "attendance_date",
            "attendance_status",
            "check_in_time",
            "check_out_time",
            "working_hours",
            "overtimee_hours",
            "remarks",
            "created_at",
            "updated_at",
        ]
        read_only_fileds = [
            "working_hours",
            "over_time",
            "created_at",
            "updated_at",
        ]

        def get_employee_name(self, obj):
            return f"{obj.employee.first_name}{obj.employee.last_name}"
        
class AttendanceCheckInSerializer(serializers.Serializer):
    remarks = serializers.CharField(required=False,allow_blank=True)

class AttendanceCheckOutSerializer(serializers.Serializer):
    break_hours = serializers.DecimalField(max_digits=5,decimal_places=2,required=False,default=0)
    remarks = serializers.CharField(required=False,allow_blank=True)

class AttendanceSummarySerializer(serializers.Serializer):
    total_days = serializers.IntegerField()
    present_days = serializers.IntegerField()
    absent_days = serializers.IntegerField()
    leave_days = serializers.IntegerField()
    work_from_home = serializers.IntegerField()
    total_working_days = serializers.DecimalField(max_digits=8,decimal_places=2)
    total_overtime_hours = serializers.DecimalField(max_digits=8,decimal_places=2)

class MonthlyAttendanceReportSerializer(serializers.Serializer):
    month = serializers.IntegerField()
    year = serializers.IntegerField()
    total_working_days = serializers.IntegerField()
    present_days = serializers.IntegerField()
    absent_days = serializers.IntegerField()
    leave_days = serializers.IntegerField()
    work_from_home_days = serializers.IntegerField()
    half_days = serializers.IntegerField()
    holiday_days = serializers.IntegerField()
    weekend_days = serializers.IntegerField()
    total_working_hours = serializers.DecimalField(max_digits=8,decimal_places=2)
    total_overtime_hours = serializers.DecimalField(max_digits=8,decimal_places=2)

class AttendanceDashboardSerializer(serializers.Serializer):
    date = serializers.DateField()
    total_attendance = serializers.IntegerField()
    present_count = serializers.IntegerField()
    absent_count = serializers.IntegerField()
    late_employees = serializers.IntegerField()
    employees_not_checked_out = serializers.IntegerField()
    average_working_hours = serializers.DecimalField(max_digits=5,decimal_places=2)

class DepartmentAttendanceSerializer(serializers.Serializer):
    department = serializers.CharField()
    present = serializers.IntegerField()
    absent = serializers.IntegerField()
    percentage = serializers.FloatField()

class EmployeePerformanceSerializer(serializers.Serializer):
    employee_id = serializers.CharField()
    employee_name = serializers.CharField()
    attendance_percentage = serializers.FloatField()
    average_working_hours = serializers.DecimalField(max_digits=6,decimal_places=2)
    total_overtime = serializers.DecimalField(max_digits=6,decimal_places=2)
    late_arrivals = serializers.IntegerField()
