import csv
from django.contrib import admin

from django.http import HttpResponse
from .models import Employee, Department, EmployeeProfile, BlockedIP

def active_employees(modeladmin,request,queryset):
    queryset.update(is_active=True)
    
active_employees.short_description = "Active Selected Employees"

def deactive_employees(modeladmin,request,queryset):
    queryset.update(is_active=False)
deactive_employees.short_description = "Deactivate Selected Employees"

def export_employees_csv(modeladmin,request,queryset):
    response = HttpResponse(content_type = "text/csv")
    response["Content-Disposition"] = 'attachment; filename="employees.csv'
    writer = writer.csv(response)
    
    writer.writerow([
        "Employee_ID",
        "First_name",
        "Last_name",
        "Department",
        "Email",
        "Salary",
        "Designation",
        "Joining Date",
        "Active"
    ])
    
    
    for employee in queryset:
        writer.writerow([
            employee.employee_id,
            employee.first_name,
            employee.last_name,
            employee.salary,
            employee.email,
            employee.department,
            employee.designation,
            employee.is_active,
            employee.joining_date
        ])
    return response

export_employees_csv.short_description = "Exported Selected Employees   "

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id","name","created_at")
    search_fields = ("name",)
    
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "employee_id",
        "first_name",
        "last_name",
        "email",
        "department",
        "designation",
        "salary",
        "is_active",
        "joining_date",       
    )
    search_fields = (
        "employee_id",
        "first_name",
        "last_name",
        "email",
    )
    list_filter = (
        "department",
        "designation",
        "is_active",
    )
    date_hierarchy = "joining_date"
    
    readonly_fields = (
        "created_at",
        "updated_at",
        "previous_salary",
        "previous_department",
    )
    actions = [
        active_employees,
        deactive_employees,
        export_employees_csv,
    ]
@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ("employee", "blood_group")
    
@admin.register(BlockedIP)
class BlockedIPAdmin(admin.ModelAdmin):
    list_display = ("ip_address","reason","created_at")