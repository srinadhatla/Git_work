from django.urls import path
from .views import (EmployeeReportView,AttendanceReportView,LeaveReportView,PayrollReportView)

urlpatterns = [
    path("employees/",EmployeeReportView.as_view(),name="employee-report"),
    path("attendance/",AttendanceReportView.as_view(),name="attendance-report"),
    path("leaves/",LeaveReportView.as_view(),name="leave-report"),
    path("payroll/",PayrollReportView.as_view(),name="payroll-report"),
]