from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        read_only_fields = [
            "created_at",
            "updated_at"
        ]

        def validate_salary(self, value):
            if value<=0:
                raise serializers.ValidationError("Salary must be greated than zero.")
            return value