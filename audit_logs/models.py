from django.db import models
from django.contrib.auth.models import User


class AuditLog(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    action = models.CharField(max_length=100)
    module = models.CharField(max_length=100)
    object_id = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True,blank=True)
    request_method = models.CharField(max_length=10,blank=True)

    def __str__(self):
        return f"{self.action} - {self.module}" 