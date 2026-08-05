from datetime import date, time
from decimal import Decimal
from django.db import transaction
from django.db.models import Sum, Count, Avg, Q
from django.utils import timezone
from attendance.models import Attendance
from attendance.validators import (
    validate_attendance_date,
    validate_duplicate_attendance,
    validate_checkout,
    validate_payroll_lock,
    validate_check_in_exists,
    validate_check_out_exists,
)

STANDARD_WORKING_HOURS = Decimal("8.00")

class AttendanceService:
    @staticmethod
    @transaction.atomic
    def check_in(employee, remarks=""):
        if employee.status != "Active":
            raise ValueError("Employee is inactive.")
        today = timezone.localdate()
        validate_attendance_date(today)
        validate_duplicate_attendance(employee,today)
        attendance = Attendance.objects.create(
            employee=employee,
            attendance_date=today,
            check_in_time=timezone.now(),
            remarks=remarks,
            attendance_status=Attendance.AttendanceStatus.PRESENT
        )
        return attendance
    
    @staticmethod
    @transaction.atomic
    def check_out(employee, break_hours=0, remarks=""):
        today = date.today()
        attendance = Attendance.objects.filter(employee=employee,attendance_date=today).first()

        validate_check_in_exists(attendance)
        validate_check_out_exists(attendance)

        if not attendance:
            raise ValueError("Check-In not found.")

        if attendance.check_out_time:
            raise ValueError("Already checked out.")

        attendance.check_out_time = timezone.now()
        validate_checkout(attendance.check_in_time, attendance.check_out_time)
        validate_payroll_lock(attendance)
        attendance.break_hours = Decimal(str(break_hours))
        attendance.working_hours = (
            AttendanceService.calculate_working_hours(
                attendance.check_in_time,
                attendance.check_out_time,
                attendance.break_hours
            )
        )

        attendance.overtime_hours = (
            AttendanceService.calculate_overtime(
                attendance.working_hours
            )
        )

        attendance.remarks = remarks or attendance.remarks
        attendance.save()
        return attendance

    @staticmethod
    def calculate_working_hours(check_in,check_out,break_hours):
        total_hours = Decimal((check_out - check_in).total_seconds() / 3600)
        working_hours = total_hours - Decimal(str(break_hours))
        if working_hours < 0:
            working_hours = Decimal("0.00")
        return round(working_hours, 2)

    @staticmethod
    def calculate_overtime(working_hours):
        if working_hours > STANDARD_WORKING_HOURS:
            return round(working_hours - STANDARD_WORKING_HOURS,2)
        return Decimal("0.00")

    @staticmethod
    def attendance_summary(employee):
        queryset = Attendance.objects.filter(employee=employee)
        return {"total_days": queryset.count(),
            "present_days": queryset.filter(attendance_status=Attendance.AttendanceStatus.PRESENT).count(),
            "absent_days": queryset.filter(attendance_status=Attendance.AttendanceStatus.ABSENT).count(),
            "leave_days": queryset.filter(attendance_status=Attendance.AttendanceStatus.ON_LEAVE).count(),
            "work_from_home_days": queryset.filter(attendance_status=Attendance.AttendanceStatus.WORK_FROM_HOME).count(),
            "total_working_hours":
                queryset.aggregate(total=Sum("working_hours"))["total"] or Decimal("0.00"),
            "total_overtime_hours":
                queryset.aggregate(total=Sum("overtime_hours"))["total"] or Decimal("0.00"),
        }

    @staticmethod
    def monthly_report(month, year):
        queryset = Attendance.objects.filter(
            attendance_date__month=month,
            attendance_date__year=year
        )
        report = {
            "month": int(month),
            "year": int(year),
            "total_working_days": queryset.count(),
            "present_days": queryset.filter(attendance_status=Attendance.AttendanceStatus.PRESENT).count(),
            "absent_days": queryset.filter(attendance_status=Attendance.AttendanceStatus.ABSENT).count(),
            "leave_days": queryset.filter(attendance_status=Attendance.AttendanceStatus.ON_LEAVE).count(),
            "work_from_home_days": queryset.filter(attendance_status=Attendance.AttendanceStatus.WORK_FROM_HOME).count(),
            "half_days": queryset.filter(attendance_status=Attendance.AttendanceStatus.HALF_DAY).count(),
            "holiday_days": queryset.filter(attendance_status=Attendance.AttendanceStatus.HOLIDAY).count(),
            "weekend_days": queryset.filter(attendance_status=Attendance.AttendanceStatus.WEEKEND).count(),

            "total_working_hours":
                queryset.aggregate(total=Sum("working_hours"))["total"] or 0,
            "total_overtime_hours":
                queryset.aggregate(total=Sum("overtime_hours"))["total"] or 0,}
        
        return report

    @staticmethod
    def dashboard_summary():
        today = date.today()
        queryset = Attendance.objects.filter(attendance_date=today)
        present_count = queryset.filter(attendance_status=Attendance.AttendanceStatus.PRESENT).count()
        absent_count = queryset.filter(attendance_status=Attendance.AttendanceStatus.ABSENT).count()
        late_count = queryset.filter(check_in_time__time__gt=time(9, 15)).count()
        not_checked_out = queryset.filter(check_out_time__isnull=True).count()
        average_hours = queryset.aggregate(avg=Avg("working_hours"))["avg"] or Decimal("0.00")

        return {
            "date": today,
            "total_attendance": queryset.count(),
            "present_count": present_count,
            "absent_count": absent_count,
            "late_employees": late_count,
            "employees_not_checked_out": not_checked_out,
            "average_working_hours": average_hours,
        }

    @staticmethod
    def department_attendance():
        queryset = (Attendance.objects.select_related("employee__department").values("employee__department__name").annotate(
                total=Count("id"),
                present=Count("id",filter=Q(attendance_status=Attendance.AttendanceStatus.PRESENT)),
                absent=Count("id",filter=Q(attendance_status=Attendance.AttendanceStatus.ABSENT)),)
        )

        report = []
        for item in queryset:
            percentage = 0
            if item["total"] > 0:
                percentage = round((item["present"] / item["total"]) * 100,2
                )

            report.append({
                "department": item["employee__department__name"],
                "present": item["present"],
                "absent": item["absent"],
                "percentage": percentage,
            })

        return report

    @staticmethod
    def employee_performance():
        queryset = (
            Attendance.objects
            .select_related("employee")
            .values(
                "employee__employee_id",
                "employee__first_name",
                "employee__last_name",
            )
            .annotate(
                total_days=Count("id"),
                present_days=Count("id",filter=Q(attendance_status=Attendance.AttendanceStatus.PRESENT)),
                average_hours=Avg("working_hours"),
                overtime=Sum("overtime_hours"),
                late_arrivals=Count("id",filter=Q(check_in_time__time__gt=time(9, 15))),)
        )
        results = []
        for row in queryset:
            attendance_percentage = 0
            if row["total_days"] > 0:
                attendance_percentage = round((row["present_days"] / row["total_days"]) * 100,2)

            results.append({
                "employee_id": row["employee__employee_id"],
                "employee_name":
                    f"{row['employee__first_name']} "
                    f"{row['employee__last_name']}",

                "attendance_percentage":
                    attendance_percentage,
                "average_working_hours":
                    row["average_hours"] or 0,
                "total_overtime":
                    row["overtime"] or 0,
                "late_arrivals":
                    row["late_arrivals"],
            })

        return results