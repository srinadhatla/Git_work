from django.urls import path
from .views import (
    AttendanceDetailAPIView,
    AttendanceListAPIView,
    AttendanceReportAPIView,
    CheckInAPIView,
    CheckOutAPIView,
    MyAttendanceAPIView,
    MyAttendanceSummaryAPIView,
    AttendanceDashboardAPIView,
    DepartmentAttendanceAPIView,
    EmployeePerformanceAPIView,
)

urlpatterns = [
    path("check-in/",CheckInAPIView.as_view(),name="attendance-check-in"),
    path("check-out/",CheckOutAPIView.as_view(),name="attendance-check-out"),
    path("my-attendance/",MyAttendanceAPIView.as_view(),name="my-attendance"),
    path("my-summary/",MyAttendanceSummaryAPIView.as_view(),name="my-summary"),
    path("",AttendanceListAPIView.as_view(),name="attendance-list"),
    path("<int:pk>/",AttendanceDetailAPIView.as_view(),name="attendance-detail"),
    path("report/",AttendanceReportAPIView.as_view(),name="attendance-report"),
    path("dashboard/",AttendanceDashboardAPIView.as_view(),name="attendance-dashboard"),
    path("analytics/departments/",DepartmentAttendanceAPIView.as_view(),name="department-attendance"),
    path("analytics/employees/",EmployeePerformanceAPIView.as_view(),name="employee-performance"),
]