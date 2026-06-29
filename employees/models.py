from django.db import models
from departments.models import Department

from django.core.exceptions import ValidationError
from django.utils import timezone

from django.db.models import Q

class Meta:
    constraints = [models.CheckConstraint(condition=Q(salary__gt=10000),name='salary__gt_10000')]
    indexes = [models.Index(fields=['email'],name='idx_employee_email'),models.Index(fields=['department','salary'],name='idx_department_salary')]         


def validate_joining_date(value):
    if value > timezone.now().date():
        raise ValidationError("Joining date cannot be in future")


class Employee(models.Model):
    employee_id = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField(validators=[validate_joining_date])
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    phone = models.CharField(max_length=15)
    designation = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    profile_image = models.ImageField(upload_to='employees/', blank=True, null=True)
    joining_date = models.DateField(validators=[validate_joining_date])

    def __str__(self):
        return f"{self.employee_id} - {self.first_name}"
        
    

class Meta:
    indexes = [
        models.Index(fields=['employee_id']),
        models.Index(fields=['email']),
        models.Index(fields=['department']),
        models.Index(fields=['joining_date']),
        models.Index(fields=['salary']),
    ]

    


