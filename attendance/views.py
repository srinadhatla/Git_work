from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import AttendanceSerializer
from .models import Attendance
from .filters import AttendanceFilter

class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.select_related(
        "employee",
        "employee__department"
    )
    serializer_class = AttendanceSerializer
    filterset_class = AttendanceFilter
    search_fields = [
        "employee__empoyee_id",
        "employee__first_name",
        "employee__last_name",
    ]
    ordering_fileds = [
        "date",
        "check_in",
        "check_out",
    ]
    ordering = ["-date"]

