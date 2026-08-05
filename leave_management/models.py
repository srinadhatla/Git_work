from django.db import models
from employees.models import Employee
from django.core.exceptions import ValidationError

from django.core.exceptions import ValidationError
from employees.models import Employee

class LeaveRequest(models.Model):

    LEAVE_TYPES = (
        ("SICK", "Sick Leave"),
        ("CASUAL", "Casual Leave"),
        ("EARNED", "Earned Leave"),
        ("OTHER", "Other Leave"),
    )

    class Status(models.TextChoices):
        PENDING_MANAGER = "PENDING_MANAGER", "Pending Manager Approval"
        PENDING_HR = "PENDING_HR", "Pending HR Approval"
        APPROVED = "APPROVED", "Approved"
        REJECTED = "REJECTED", "Rejected"

    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="leave_requests")
    leave_type = models.CharField(max_length=20,choices=LEAVE_TYPES)
    reason = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    total_days = models.DecimalField(max_digits=5,decimal_places=1,default=0)
    status = models.CharField(max_length=30,choices=Status.choices,default=Status.PENDING_MANAGER)
    manager_comment = models.TextField(blank=True,null=True)
    hr_comment = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "leave_requests"
        ordering = ["employee", "leave_type"]
        unique_together = ("employee", "leave_type", "start_date")
        verbose_name = "Leave Balance"
        verbose_name_plural = "Leave Balances"

    def __str__(self):
        return f"{self.employee} - {self.leave_type}"

class LeaveType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True)
    annual_quota = models.PositiveIntegerField(default=0)
    is_paid = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "leave_types"
        ordering = ["name"]
        verbose_name = "Leave Type"
        verbose_name_plural = "Leave Types"

    def __str__(self):
        return f"{self.name} ({self.code})"

class LeaveBalance(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="leave_balances")
    leave_type = models.ForeignKey(LeaveType,on_delete=models.CASCADE,related_name="balances")
    year = models.PositiveIntegerField()
    allocated_days = models.DecimalField(max_digits=5,decimal_places=1,default=0)
    used_days = models.DecimalField(max_digits=5,decimal_places=1,default=0)
    remaining_days = models.DecimalField(max_digits=5,decimal_places=1,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "leave_balances"
        unique_together = ("employee", "leave_type", "year")
        ordering = ["employee", "leave_type"]
        verbose_name = "Leave Balance"
        verbose_name_plural = "Leave Balances"

    def clean(self):
        if self.used_days > self.allocated_days:
            raise ValidationError("Used leave cannot exceed allocated leave.")

    def save(self, *args, **kwargs):
        self.remaining_days = self.allocated_days - self.used_days
        super().save(*args, **kwargs)

    def __str__(self):
        return (f"{self.employee.employee_id} - "f"{self.leave_type.code} ({self.year})")