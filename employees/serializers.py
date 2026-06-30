from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'id',
            'employee_id',
            'first_name',
            'email'
        ]
        
class EmployeeSerializer(serializers.ModelSerializer):
    def validate_salary(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Salary cannot be negative"
            )
        return value

def validate_email(self, value):
    if Employee.objects.filter(email=value).exists():
        raise serializers.ValidationError("Email already exists")
    return value

def validate_employee_id(self, value):
    if Employee.objects.filter(employee_id=value).exists():
        raise serializers.ValidationError("Employee ID already exists")
    return value



def validate_phone(self, value):
    if len(value) != 10:
        raise serializers.ValidationError("Phone number must contain 10 digits")
    return value