from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import LeaveRequest, LeaveBalance
from .serializers import (
    LeaveRequestSerializer,
    LeaveBalanceSerializer,
    LeaveApplySerializer,
)
from .services.leave_service import LeaveService
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import LeaveRequestFilter
from .permissions import (IsHR)
from rest_framework.views import APIView

from django.http import HttpResponse
from .utils import (export_leave_history_pdf,export_leave_register_excel,export_leave_transactions_csv,)

class ApplyLeaveView(generics.CreateAPIView):
    serializer_class = LeaveApplySerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        LeaveService.apply_leave(
            employee=request.user.employee,
            user=request.user,
            leave_type=serializer.validated_data["leave_type"],
            start_date=serializer.validated_data["start_date"],
            end_date=serializer.validated_data["end_date"],
            reason=serializer.validated_data["reason"],
        )
        return Response(LeaveRequestSerializer(leave).data,status=status.HTTP_201_CREATED,)

class MyLeaveListView(generics.ListAPIView):
    serializer_class = LeaveRequestSerializer
    permission_classes = [
        IsAuthenticated,
        IsHR,
    ]

    queryset = LeaveRequest.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_class = LeaveRequestFilter
    search_fields = [
        "employee__employee_id",
        "employee__first_name",
        "employee__last_name",
        "reason",
    ]

    ordering_fields = [
        "start_date",
        "end_date",
        "created_at",
        "approved_at",
    ]

    ordering = [
        "-created_at",
    ]

class MyLeaveBalanceView(generics.ListAPIView):
    serializer_class = LeaveBalanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return LeaveBalance.objects.filter(employee=self.request.user.employee)

class CancelLeaveView(generics.ListAPIView):
    serializer_class = LeaveRequestSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        leave = get_object_or_404(LeaveRequest, id=kwargs["pk"],employee=request.user.employee,)
        LeaveService.cancel_leave(leave)
        return Response(LeaveRequestSerializer(leave).data)

class PendingLeaveView(generics.ListAPIView):
    serializer_class = LeaveRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return LeaveRequest.objects.filter(status=LeaveRequest.Status.PENDING)

class ApproveLeaveView(generics.UpdateAPIView):
    serializer_class = LeaveRequestSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        leave = get_object_or_404(LeaveRequest,pk=kwargs["pk"],)
        LeaveService.approve_leave(leave,approver_type="manager",)
        return Response(LeaveRequestSerializer(leave).data)

class RejectLeaveView(generics.UpdateAPIView):
    serializer_class = LeaveRequestSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        leave = get_object_or_404(LeaveRequest,pk=kwargs["pk"],)
        LeaveService.reject_leave(leave,request.data.get("comment"),)
        return Response(LeaveRequestSerializer(leave).dat)

class LeaveListView(generics.ListAPIView):
    serializer_class = LeaveRequestSerializer
    permission_classes = [IsAuthenticated]
    queryset = LeaveRequest.objects.all().order_by("-created_at")

class FinalApproveLeaveView(generics.UpdateAPIView):
    serializer_class = LeaveRequestSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        leave = get_object_or_404(LeaveRequest,pk=kwargs["pk"],)
        LeaveService.approve_leave(leave,approver_type="hr",)
        return Response(LeaveRequestSerializer(leave).data)

class MonthlyLeaveCalendarView(APIView):
    permission_classes = [IsAuthenticated,IsHR,]
    def get(self, request):
        year = request.query_params.get("year")
        month = request.query_params.get("month")
        queryset = LeaveService.monthly_leave_calendar(year,month,)
        serializer = LeaveRequestSerializer(queryset,many=True,)
        return Response(serializer.data)

class UpcomingLeavesView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = LeaveService.upcoming_leaves()
        serializer = LeaveRequestSerializer(queryset,many=True)
        return Response(serializer.data)

class EmployeesOnLeaveTodayView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = LeaveService.employees_on_leave_today()
        serializer = LeaveRequestSerializer(queryset,many=True,)
        return Response(serializer.data)

class LeaveDashboardView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        return Response(LeaveService.dashboard_summary())

class CompanyAnalyticsView(APIView):
    permission_classes = [IsAuthenticated,IsHR,]
    def get(self, request):
        year = request.query_params.get("year")
        return Response(LeaveService.company_leave_analytics(year)
        )

class LeaveHistoryPDFView(APIView):
    permission_classes = [IsAuthenticated,IsHR,]
    def get(self, request):
        queryset = LeaveRequest.objects.all()
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = 'attachment; filename="leave_history.pdf"'
        return export_leave_history_pdf(queryset,response,)
class LeaveRegisterExcelView(APIView):
    permission_classes = [IsAuthenticated,IsHR,]
    def get(self, request):
        workbook = export_leave_register_excel(LeaveRequest.objects.all())
        response = HttpResponse(
            content_type=("application/vnd.openxmlformats-officedocument.""spreadsheetml.sheet"))

        response["Content-Disposition"] = 'attachment; filename="leave_register.xlsx"'
        workbook.save(response)
        return response

class LeaveTransactionsCSVView(APIView):
    permission_classes = [IsAuthenticated,IsHR,]
    def get(self, request):
        return export_leave_transactions_csv(LeaveRequest.objects.all())