from rest_framework.views import APIView
from rest_framework.response import Response

from employees.models import Employee
from attendance.models import Attendance
from leave_management.models import LeaveRequest
from payroll.models import Payroll

class EmployeeReportView(APIView):
    def get(self, request):
        data = {
            "total_employees": Employee.objects.count(),
            "active_employees": Employee.objects.filter(status="Active").count(),
            "inactive_employees": Employee.objects.filter(status="Inactive").count(),
        }
        return Response(data)

class AttendanceReportView(APIView):
    def get(self, request):
        data = {
            "total_attendance":
                Attendance.objects.count(),

            "present":
                Attendance.objects.filter(status="Present").count(),

            "absent":
                Attendance.objects.filter(status="Absent").count(),

            "leave":
                Attendance.objects.filter(status="Leave").count(),

            "work_from_home":
                Attendance.objects.filter(status="WFH").count(),
        }

        return Response(data)



class LeaveReportView(APIView):
    def get(self, request):
        data = {

            "total_leave_requests":
                LeaveRequest.objects.count(),

            "pending":
                LeaveRequest.objects.filter(status="PENDING_MANAGER").count(),

            "approved":
                LeaveRequest.objects.filter(status="APPROVED").count(),

            "rejected":
                LeaveRequest.objects.filter(status="REJECTED").count(),
        }

        return Response(data)

class PayrollReportView(APIView):
    def get(self, request):
        total_salary = 0
        payrolls = Payroll.objects.all()
        for payroll in payrolls:
            total_salary += payroll.salary

        data = {

            "total_payroll_records":
                Payroll.objects.count(),

            "total_salary_paid":
                total_salary,
        }

        return Response(data)