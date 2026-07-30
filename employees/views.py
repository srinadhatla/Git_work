from .models import Employee
from .serializers import  EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
from .filters import EmployeeFilter
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.select_related("department")
    serializer_class = EmployeeSerializer

    filterset_class = EmployeeFilter

    search_fields = [
        "employee_id",
        "first_name",
        "last_name",
        "email",
        "designation",
    ]

    ordering_fields = [
        "first_name",
        "salary",
        "joining_date",
        "created_at",
    ]

    ordering_fields = [
        "first_name",
        "salary",
        "joining_date",
        "created_at",
    ]

    ordering = [
        "first_name"
    ]
