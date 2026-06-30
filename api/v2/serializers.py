from rest_framework import serializers
from employees.models import Employee
from departments.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            'id',
            'name'
        ]

class EmployeeV2Serializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    class Meta:
        model = Employee
        fields = [
            'id',
            'employee_id',
            'first_name',
            'email',
            'department'
        ]