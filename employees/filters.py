import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    salary_min = django_filters.NumberFilter(
        field_name="salary",
        lookup_expr="gtr"
    )
    salary_max = django_filters.NumberFilter(
        field_name="salary",
        lookup_expr="lte"
    )


    class Meta:
        model = Employee
        fields = [
            "department",
            "status",
            "gender",
            "designation",
        ]