from django.db import models


class AuditLog(models.Model):
    user = models.CharField(max_length=100)
    action = models.CharField(max_length=100)
    module = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True,blank=True)

    def __str__(self):
        return f"{self.action} - {self.module}"