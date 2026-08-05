from django.urls import path
from .views import (
    ApplyLeaveView,
    MyLeaveListView,
    MyLeaveBalanceView,
    CancelLeaveView,
    PendingLeaveView,
    ApproveLeaveView,
    RejectLeaveView,
    LeaveListView,
    FinalApproveLeaveView,
    MonthlyLeaveCalendarView,
    UpcomingLeavesView,
    EmployeesOnLeaveTodayView,
    LeaveDashboardView,
    CompanyAnalyticsView,
    LeaveHistoryPDFView,
    LeaveRegisterExcelView,
    LeaveTransactionsCSVView,
)


app_name = "leave_management"

urlpatterns = [
    path("apply/",ApplyLeaveView.as_view(),name="apply_leave",),
    path("my-leaves/",MyLeaveListView.as_view(),name="my_leaves",),
    path("my-balance/",MyLeaveBalanceView.as_view(),name="my_balance",),
    path("<int:pk>/cancel/",CancelLeaveView.as_view(),name="cancel_leave",),
    path("pending/",PendingLeaveView.as_view(),name="pending_leaves",),
    path("<int:pk>/approve/",ApproveLeaveView.as_view(),name="approve_leave",),
    path("<int:pk>/reject/",RejectLeaveView.as_view(),name="reject_leave",),
    path("",LeaveListView.as_view(),name="leave_list",),
    path("<int:pk>/final-approve/",FinalApproveLeaveView.as_view(),name="final_approve",),
    path("calendar/",MonthlyLeaveCalendarView.as_view(),name="leave_calendar",),
    path("upcoming/",UpcomingLeavesView.as_view(),name="upcoming_leaves",),
    path("today/",EmployeesOnLeaveTodayView.as_view(),name="employees_on_leave_today",),
    path("dashboard/",LeaveDashboardView.as_view(),name="leave_dashboard",),
    path("analytics/",CompanyAnalyticsView.as_view(),name="leave_analytics",),
    path("reports/pdf/",LeaveHistoryPDFView.as_view(),name="leave_pdf",),
    path("reports/excel/",LeaveRegisterExcelView.as_view(),name="leave_excel",),
    path("reports/csv/",LeaveTransactionsCSVView.as_view(),name="leave_csv",),
]