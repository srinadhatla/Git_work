import random
from datetime import date, timedelta

from django.core.management.base import BaseCommand

from employees.models import Department, Employee

class Command(BaseCommand):
    help = "Generate sample department and employees"
    
    def handle(self, *args, **kwargs):
        departments = [
            "HR",
            "Finanace",
            "IT",
            "Marketing",
            "Operations",
            "Support",
            "Admin",
            "Security",
            "Testing",
        ]
        
        department_objects = []
    
        for dept in departments:
            department, created = Department.objects.get_or_create(name=dept,defaults={"description": f"{dept} Department"},)
            department_objects.append(department)
            
        self.stdout.write(self.style.SUCCESS("Departments created."))
        
        designations = [
            "manager",
            "Python Developer",
            "Tester",
            "HR Exceutive",
            "Team Lead",
        ]
        
        for i in range(1, 101):
            Employee.objects.get_or_create(
                employee_id=f"EMP{i:03}",
                defaults={
                    "first_name": f"Employee{i}",
                    "last_name" : "Demo",
                    "email" : f"employee{i}@blackroth.in",
                    "phone" : f"914562{i:04}",
                    "department" : random.choice(department_objects),
                    "designation" : random.choice(designations),
                    "salary" : random.randint(25000,100000),
                    "joining_date" : date.today() - timedelta(days=random.randint(1,365)),
                    "is_active" : True,
                },
            )
            
        self.stdout.write(self.style.SUCCESS("100 Employees created successfully."))