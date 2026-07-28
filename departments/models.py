from django.db import models
from django.conf import settings


class Department(models.Model):

    name = models.CharField(max_length=100,unique=True)
    code = models.CharField(max_length=20,unique=True)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True,related_name="managed_departments")
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name