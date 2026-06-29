from django.db import models
from employees.models import Employee


class AuditLog(models.Model):
    action = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    old_value = models.DecimalField(max_digits=10, decimal_places=2)
    new_value = models.DecimalField(max_digits=10, decimal_places=2)
    performed_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)