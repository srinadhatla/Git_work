from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.signals import user_logged_in, user_logged_out

from .models import Employee, EmployeeProfile, Department
from audit_logs.models import AuditLog

import logging


@receiver(post_save, sender=Employee)
def create_employee_profile(sender, instance, created, **kwargs):
    """
    Create EmployeeProfile and AuditLog when a new Employee is created.
    """
    if created:
        EmployeeProfile.objects.create(employee=instance)
        app_logger.info(f"Emplyee Created: {instance.employee_id} - {instance.first_name}")

        AuditLog.objects.create(
            user=None,
            action="Employee Created",
            module="Employee",
            object_id=instance.id,
            request_method="SYSTEM"
        )

        print(f"Welcome {instance.first_name}! Employee Profile Created.")

    else:
        AuditLog.objects.create(
            user=None,
            action="Employee Updated",
            module="Employee",
            object_id=instance.id,
            request_method="SYSTEM"
        )
        app_logger.info(f"Employee Updated: {instance.employee_id}")

        print(f"{instance.first_name} updated successfully.")
        


@receiver(pre_save, sender=Employee)
def track_employee_changes(sender, instance, **kwargs):
    """
    Store previous salary and department before update.
    """

    if not instance.pk:
        return

    try:
        old_employee = Employee.objects.get(pk=instance.pk)

        if old_employee.salary != instance.salary:
            instance.previous_salary = old_employee.salary

        if old_employee.department != instance.department:
            if old_employee.department:
                instance.previous_department = old_employee.department.name

    except Employee.DoesNotExist:
        pass
    
@receiver(post_save, sender=Department)
def department_created(sender, instance, created, **kwargs):
    """
    Create AuditLog whenever a Department is created.
    """

    if created:
        AuditLog.objects.create(
            user=None,
            action="Department Created",
            module="Department",
            object_id=instance.id,
            request_method="SYSTEM"
        )

        print(f"Department '{instance.name}' created successfully.")


@receiver(post_delete, sender=Employee)
def employee_deleted(sender, instance, **kwargs):
    """
    Create AuditLog when Employee is deleted.
    """

    AuditLog.objects.create(
        user=None,
        action="Employee Deleted",
        module="Employee",
        object_id=instance.id,
        request_method="SYSTEM"
    )

    print(f"{instance.first_name} archived successfully.")
    
    
    
@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    AuditLog.objects.create(
        user=user,
        action="User Login",
        module="Authentication",
        object_id=user.id,
        ip_address=request.META.get("REMOTE_ADDR"),
        request_method=request.method,
    )

    print(f"{user.username} logged in.")
    
    
@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    AuditLog.objects.create(
        user=user,
        action="User Logout",
        module="Authentication",
        object_id=user.id if user else 0,
        ip_address=request.META.get("REMOTE_ADDR"),
        request_method=request.method if request else "",
    )

    if user:
        print(f"{user.username} logged out.")
        
        
app_logger = logging.getLogger("application")
error_logger = logging.getLogger("error")
security_logger = logging.getLogger("security")