import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db.models import Avg, Max, Min

from employees.models import Department, Employee

class Command(BaseCommand):
    help = "Generate HRMS reports"
    
    def handle(self, *args, **kwargs):
        reports_dir = os.path.join(settings.BASE_DIR, "reports")
        os.makedirs(reports_dir, exist_ok=True)
        
        
        employee_file = os.path.join(
            reports_dir,
            "employees_summary.txt"
        )
        
        with open(employee_file, "w") as file:
            file.write("EMPLOYEE SUMMARY\n")
            file.write("=" *40 + "\n\n")
            
            file.write(f"Total Employees : {Employee.objects.count()}\n")
            
            file.write(
                f"Active Employees : "
                f"{Employee.objects.filter(is_active=True).count()}\n"
            )
            file.write(
                f"Inactive Employees : "
                f"{Employee.objects.filter(is_active=False).count()}\n" 
            )
            
        department_file = os.path.join(
            reports_dir,
            "department_summary.txt"
        )
        with open(department_file, "w") as file:
            file.write("DEPARTMENT SUMMARY\n")
            file.write("=" * 40 + "\n\n")
            
            for department in Department.objects.all():
                count = Employee.objects.filter(
                    department=department
                ).count()
                file.write(f"{department.name} : {count} Employee\n")
                
        salary_file = os.path.join(
            reports_dir,
            'salary_summary.txt'
        )
        salary = Employee.objects.aggregate(
            average=Avg("salary"),
            highest=Max("salary"),
            lowest=Min("salary")
        )
        with open(salary_file, "w") as file:
            file.write(f"Average Salary : {salary['average']}\n")
            file.write(f"Highest Salary : {salary['highest']}\n")
            file.write(f"lowest Salary : {salary['lowest']}\n")
            
        self.stdout.write(
            self.style.SUCCESS("Reports Generated Successfully")
        )