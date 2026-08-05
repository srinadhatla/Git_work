import django_filters
from .models import LeaveRequest

class LeaveRequestFilter(django_filters.FilterSet):
    employee = django_filters.CharFilter(
        field_name="employee__employee_id",
        lookup_expr="iexact",
    )

    department = django_filters.CharFilter(
        field_name="employee__department__name",
        lookup_expr="icontains",
    )

    leave_type = django_filters.CharFilter(
        field_name="leave_type__code",
        lookup_expr="iexact",
    )

    status = django_filters.CharFilter(
        lookup_expr="iexact",
    )

    year = django_filters.NumberFilter(
        field_name="start_date__year",
    )

    start_date = django_filters.DateFilter(
        field_name="start_date",
        lookup_expr="gte",
    )

    end_date = django_filters.DateFilter(
        field_name="end_date",
        lookup_expr="lte",
    )

    manager = django_filters.CharFilter(
        field_name="employee__manager__employee_id",
        lookup_expr="iexact",
    )

    class Meta:
        model = LeaveRequest
        fields = [
            "employee",
            "department",
            "leave_type",
            "status",
            "year",
            "manager",
            "start_date",
            "end_date",
        ]