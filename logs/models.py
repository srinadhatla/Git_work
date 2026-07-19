from django.db import models
from django.contrib.auth.models import User


class SecurityLog(models.Model):
    ACTION_CHOICES = [
        ("LOGIN_SUCCESS", "Login Success"),
        ("LOGIN_FAILED", "Login Failed"),
        ("PASSWORD_CHANGE", "Password Change"),
        ("PASSWORD_RESET", "Password Reset"),
        ("UNAUTHORIZED_ACCESS", "Unauthorized Access"),
        ("PERMISSION_DENIED", "Permission Denied"),
        ("TOKEN_BLACKLISTED", "Token Blacklisted"),
    ]

    STATUS_CHOICES = [
        ("SUCCESS", "Success"),
        ("FAILED", "Failed"),
    ]

    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    ip_address = models.GenericIPAddressField()
    action = models.CharField(max_length=30,choices=ACTION_CHOICES)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} - {self.status}"