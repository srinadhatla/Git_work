from django.db import models
from employees.models import Employee

class Payroll(models.Model):
    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("GENERATED", "Generated"),
        ("PAID", "Paid"),
    )
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="payroll_records")
    month = models.CharField(max_length=20)
    basic_salary = models.DecimalField(max_digits=10,decimal_places=2)
    bonus = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    deduction = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    net_salary = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee.employee_id} - {self.month}"