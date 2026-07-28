from django.db import models
from employees.models import Employee

class Attendance(models.Model):
    STATUS_CHOICES = (
        ("Present", 'Present'),
        ("Absent", "Absent"),
        ("Leave", "Leave"),
        ("WFH", "Work From Home"),
    )
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="attendance_records")
    date = models.DateField()
    check_in = models.TimeField()
    check_out = models.TimeField(null=True,blank=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="Present")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date"]
        constraints = [
            models.UniqueConstraint(
                fields=["employee", "date"],
                name="unique_employee_attendance"
            )
        ]

    def __str__(self):
        return f"{self.employee.employee_id} - {self.date}"