from rest_framework import serializers
from employees.models import Employee


class EmployeeV1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id',
            'employee_id',
            'first_name',
            'email'
        ]