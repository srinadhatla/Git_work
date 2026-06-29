from django.db import models
from django.contrib.auth.models import User
from departments.models import Department



class UserProfile(models.Model):
    
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('HR', 'HR'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    designation = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username


    @property
    def email(self):
        return self.user.email

