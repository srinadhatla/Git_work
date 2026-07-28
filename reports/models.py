from django.db import models

class Report(models.Model):

    REPORT_TYPES = (
        ("EMPLOYEE", "Employee Report"),
        ("ATTENDANCE", "Attendance Report"),
        ("LEAVE", "Leave Report"),
        ("PAYROLL", "Payroll Report"),
    )

    report_type = models.CharField(max_length=50,choices=REPORT_TYPES)
    file = models.FileField(upload_to="reports/",blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.report_type