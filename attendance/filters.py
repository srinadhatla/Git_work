import django_filters
from attendance.models import Attendance

class AttendanceFilter(django_filters.FilterSet):
    employee = django_filters.CharFilter(field_name="employee__employee_id",lookup_expr="iexact")
    department = django_filters.CharFilter(field_name="employee__department__name",lookup_expr="iexact")
    status = django_filters.CharFilter(field_name="attendance_status",lookup_expr="iexact")
    month = django_filters.NumberFilter(field_name="attendance_date__month")
    year = django_filters.NumberFilter(field_name="attendance_date__year")
    attendance_date = django_filters.DateFilter(field_name="attendance_date")

    class Meta:
        model = Attendance
        fields = [
            "employee",
            "department",
            "status",
            "month",
            "year",
            "attendance_date",
        ]