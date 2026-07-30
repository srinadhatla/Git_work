from openpyxl import Workbook
from attendance.models import Attendance

class AttendanceExcelReport:
    @staticmethod
    def daily_report(report_date):
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Daily Attendance"
        headers = [
            "Employee ID",
            "Employee Name",
            "Department",
            "Date",
            "Check In",
            "Check Out",
            "Working Hours",
            "Status",
        ]
        sheet.append(headers)
        records = Attendance.objects.select_related(
            "employee",
            "employee__department"
        ).filter(
            attendance_date=report_date
        )
        for attendance in records:
            sheet.append([
                attendance.employee.employee_id,
                f"{attendance.employee.first_name} "
                f"{attendance.employee.last_name}",
                attendance.employee.department.name,
                attendance.attendance_date,
                attendance.check_in_time,
                attendance.check_out_time,
                attendance.working_hours,
                attendance.attendance_status,
            ])

        return workbook

    @staticmethod
    def monthly_report(month, year):
        Workbook = Workbook()
        sheet = Workbook.active
        sheet.title = "Montly Attendance"
        sheet.append([
            "Employee ID",
            "Employee Name",
            "Department",
            "Date",
            "Working Hours",
            "Overtime",
            "Status",
        ])
        records =Attendance.objects.select_related("employee","employee__department").filter(attendance_date__mont=month, attendance_date__year=year)

        for attendance in records:
            sheet.append([
                attendance.employee.employee_id,
                f"{attendance.employee_.first_name}"
                f"{attendance.employee.last_name}",
                attendance.employee.department.name,
                attendance.working_hours,
                attendance.overtime_hours,
                attendance.attendance_status
            ])

        return Workbook