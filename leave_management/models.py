from django.db import models
from employees.models import Employee


class LeaveRequest(models.Model):

    LEAVE_TYPES = (
        ("SICK", "Sick Leave"),
        ("CASUAL", "Casual Leave"),
        ("EARNED", "Earned Leave"),
        ("OTHER", "Other Leave"),
    )

    STATUS_CHOICES = (
        ("PENDING_MANAGER", "Pending Manager Approval"),
        ("PENDING_HR", "Pending HR Approval"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
    )

    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="leave_requests")
    leave_type = models.CharField(max_length=20,choices=LEAVE_TYPES)
    reason = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=30,choices=STATUS_CHOICES,default="PENDING_MANAGER")
    manager_comment = models.TextField(blank=True,null=True)
    hr_comment = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.employee.employee_id} - {self.leave_type}"