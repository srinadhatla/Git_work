from rest_framework import serializers
from .models import LeaveRequest, LeaveType, LeaveBalance


class LeaveTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveType
        fields = [
            "id",
            "name",
            "code",
            "annual_quota",
            "is_paid",
            "description",
            "created_at",
            "updated_at",
        ]

class LeaveBalanceSerializer(serializers.ModelSerializer):
    leave_type_name = serializers.CharField(source="leave_type.name", read_only=True)
    leave_type_code = serializers.CharField(source="leave_type.code", read_only=True)
    employee_name = serializers.CharField(source="employee.get_full_name", read_only=True)

    class Meta:
        model = LeaveBalance
        fields = [
            "id",
            "employee",
            "leave_type",
            "leave_type_name",
            "leave_type_code",
            "allocated_days",
            "used_days",
            "remaining_days",
            "year",
        ]

class LeaveRequestSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source="employee.get_full_name", read_only=True)
    leave_type_name = serializers.CharField(source="leave_type.name", read_only=True)

    class Meta:
        model = LeaveRequest
        fields = [
            "id",
            "employee",
            "leave_type",
            "leave_type_name",
            "leave_type_code",
            "start_date",
            "end_date",
            "total_days",
            "reason",
            "status",
            "manager_comments",
            "hr_comments",
            "applied_at",
            "approved_at",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "status",
            "approved_at",
            "created_at",
            "updated_at",
        ]

class LeaveApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = [
            "leave_type",
            "start_date",
            "end_date",
            "reason",
        ]
    def validate(self, data):
        start_date = data.get("start_date")
        end_date = data.get("end_date")

        if end_date < start_date:
            raise serializers.ValidationError("End date cannot be before start date")

        return data
