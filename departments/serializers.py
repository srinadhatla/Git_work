from rest_framework import serializers

from .models import Department
from employees.serializers import EmployeeBasicSerializer


class DepartmentSerializer(serializers.ModelSerializer):

    employees = EmployeeBasicSerializer(many=True,read_only=True)
    class Meta:
        model = Department
        fields = [
            'id',
            'name',
            'description',
            'employees'
        ]