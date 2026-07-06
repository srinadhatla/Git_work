import os
from datetime import date, timedelta

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone

from employees.models import Employee

class Command(BaseCommand):
    help = "Deactivate employees whose joining date is older than 180 days"

    def handle(self, *args, **options):
        
        cutoff_date = timezone.now().date() - timedelta(days=180)
        employees = Employee.objects.filter(joining_date__lt= cutoff_date, is_active=True)
        report_path = os.path.join(
            settings.BASE_DIR,"reports","inactive_users_report.txt"
        )
        count = 0
        with open(report_path, "w") as report:
            report.write("INACTIVE USERS REPORTS\n")
            report.write("=" * 50 + "\n\n")
            
            for employee in employees:
                employee.is_active=False
                employee.save()
                
                report.write(
                    f"{employee.employee_id} - "
                    f"{employee.first_name} {employee.last_name}\n"
                )
                
                count +=1
                
            report.write("\n")
            report.write(f"Total Deactivated Employees :{count}\n")
            
        self.stdout.write(
            self.style.SUCCESS(
                f"{count} employees deactivated successfully."
            )
        )
            
            
        
        