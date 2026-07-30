from datetime import date
from django.core.exceptions import ValidationError
from attendance.models import Attendance

def validate_attendance_date(attendance_date):

    if attendance_date > date.today():
        raise ValidationError("Attendance date cannot be in the future.")


def validate_duplicate_attendance(employee, attendance_date):

    if Attendance.objects.filter(employee=employee,attendance_date=attendance_date).exists():
        raise ValidationError("Attendance already marked for this date.")

def validate_checkout(check_in_time, check_out_time):

    if check_out_time <= check_in_time:
        raise ValidationError("Check-out time must be greater than check-in time.")

def validate_payroll_lock(attendance):

    if attendance.payroll_generated:
        raise ValidationError("Attendance cannot be edited after payroll generation.")

def validate_check_in_exists(attendance):

    if attendance is None:
        raise ValidationError("Employee has not checked in today.")

def validate_check_out_exists(attendance):

    if attendance.check_out_time:
        raise ValidationError("Employee has already checked out.")