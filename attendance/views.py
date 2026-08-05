from rest_framework import status
from rest_framework.generics import (ListAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from attendance.filters import AttendanceFilter
from django_filters.rest_framework import DjangoFilterBackend


from attendance.models import Attendance
from attendance.serializers import (
    AttendanceSerializer,
    AttendanceCheckInSerializer,
    AttendanceCheckOutSerializer,
    AttendanceSummarySerializer,
    MonthlyAttendanceReportSerializer,
    AttendanceDashboardSerializer,
    DepartmentAttendanceSerializer,
    EmployeePerformanceSerializer,
)
from attendance.services.attendance_service import AttendanceService
from rest_framework.exceptions import ValidationError

class CheckInAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AttendanceCheckInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            attendance = AttendanceService.check_in(employee=request.user.employee,remarks=serializer.validated_data.get("remarks",""))
            return Response(AttendanceSerializer(attendance).data,status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)

class CheckOutAPIView(APIView): 
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AttendanceCheckOutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            attendance = AttendanceService.check_out(employee=request.user.employee,break_hours=serializer.validated_data.get("break_hours",0),remarks=serializer.validated_data.get("remarks",""))
            return Response(AttendanceSerializer(attendance).data)  
        except ValueError as e:
            return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)

class MyAttendanceAPIView(APIView):
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def get_query_set(self):
        return Attendance.objects.filter(employee=self.request.user.employee).order_by("-attendance-date")

class MyAttendanceSummaryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        summary = AttendanceService.attendance_summary(request.user.employee)
        serializer = AttendanceSummarySerializer(summary)
        return Response(serializer.data)

class AttendanceListAPIView(ListAPIView):
    queryset = Attendance.objects.select_related(
        "employee",
        "employee__department"
    )

    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]

    filterset_class = AttendanceFilter

class AttendanceDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.select_related("employee","employee__department")
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        attendance = self.get_object()
        if attendance.payroll_generated:
            raise ValidationError("Attendance cannot be edited after payroll generation")
        serializer.save()

class AttendanceReportAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        month = request.query_params.get("month")
        year = request.query_params.get("year")
        if not month or not year:
            return Response(
                {
                    "error": "month and year are required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        report = AttendanceService.monthly_report(month,year)
        serializer = MonthlyAttendanceReportSerializer(report)
        return Response(serializer.data)

class AttendanceDashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        dashboard = AttendanceService.dashboard_summary()
        serializer = AttendanceDashboardSerializer(dashboard)
        return Response(serializer.data)

class DepartmentAttendanceAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = AttendanceService.department_attendance()
        serializer = DepartmentAttendanceSerializer(data,many=True)
        return Response(serializer.data)

class EmployeePerformanceAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = AttendanceService.employee_performance()
        serializer = EmployeePerformanceSerializer(data,many=True)
        return Response(serializer.data)