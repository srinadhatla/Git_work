from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Employee

from audit_logs.models import AuditLog

from django.db.models.signals import post_delete

@receiver(post_save, sender=Employee)
def employee_created(sender,instance,created,**kwargs):
    if created:
        AuditLog.objects.create(user="System",action="CREATE",module="Employee")
        print(f"Audit Log Created for {instance.first_name}")
        

@receiver(post_delete, sender=Employee)
def employee_deleted(sender,instance,**kwargs):
    AuditLog.objects.create(
        user="System",
        action="DELETE",
        module="Employee"
    )
    print(f"Delete Log Created for {instance.first_name}")
    
@receiver(post_save, sender=Employee)
def employee_saved(sender, instance, created, **kwargs):
    if created:
        AuditLog.objects.create(user="System",action="CREATE",module="Employee")
    else:
        AuditLog.objects.create(user="System",action="UPDATE",module="Employee")        
        
        
@receiver(post_save, sender=Employee)
def employee_created_or_updated(sender, instance, created, **kwargs):
    if created:
        AuditLog.objects.create(
            user="System",
            action="CREATE",
            module="Employee"
        )
    else:
        AuditLog.objects.create(
            user="System",
            action="UPDATE",
            module="Employee"
        )