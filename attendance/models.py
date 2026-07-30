from datetime import date
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.db import models
from employees.models import Employee

class Attendance(models.Model):
    class AttendanceStatus(models.TextChoices):
        PRESENT = "Present", "Present"
        ABSENT = "Absent", "Absent"
        HALF_DAY = "Half Day", "Half Day"
        WORK_FROM_HOME = "Work From Home", "Work From Home"
        ON_LEAVE = "On Leave", "On Leave"
        HOLIDAY = "Holiday", "Holiday"
        WEEKEND = "Weekend", "Weekend"

    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="attendance_records")
    attendance_date = models.DateField()
    check_in_time = models.DateTimeField(null=True,blank=True)
    joining_date = models.DateField(null=True,blank=True)
    check_out_time = models.DateTimeField(null=True,blank=True)
    working_hours = models.DecimalField(max_digits=5,decimal_places=2,default=Decimal("0.00"))
    break_hours = models.DecimalField(max_digits=5,decimal_places=2,default=Decimal("0.00"))
    overtime_hours = models.DecimalField(max_digits=5,decimal_places=2,default=Decimal("0.00"))
    attendance_status = models.CharField(max_length=25,choices=AttendanceStatus.choices,default=AttendanceStatus.PRESENT)
    remarks = models.TextField(blank=True,null=True)
    payroll_generated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active= models.BooleanField(default=True)

    class Meta:
        ordering = ["-attendance_date", "-created_at"]
        unique_together = ("employee","attendance_date",)
        indexes = [
            models.Index(fields=["attendance_date"]),
            models.Index(fields=["attendance_status"]),
            models.Index(fields=["employee"]),
        ]

    def clean(self):
        if self.attendance_date > date.today():
            raise ValidationError("Attendance date cannot be in the future.")

        if (
            self.check_in_time
            and self.check_out_time
            and self.check_out_time <= self.check_in_time
        ):
            raise ValidationError("Check-out time must be greater than check-in time.")

        if self.working_hours < 0:
            raise ValidationError("Working hours cannot be negative.")

    def __str__(self):
        return (f"{self.employee.employee_id} - "f"{self.attendance_date}")