from django import forms
from .models import Employee
import re
from datetime import date

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'
        
def clean_employee_id(self):
    employee_id = self.cleaned_data['employee_id']
    if not re.match(r'^EMP\d+$', employee_id):
        raise forms.ValidationError("Employee ID must be start with EMP and followed by Numbers")
    return employee_id

def clean_email(self):
    email = self.clean_data['email']
    if Employee.objects.filter(email=email).exists():
        raise forms.ValidationError("Employee email aready exists")
    return email

def clean_salary(self):
    salary = self.cleaned_data["salary"]
    if salary<10000:
        raise forms.ValidationError("salary must greated than 10000")
    elif salary>500000:
        raise forms.ValidationError("salary cannot exceed more than 500000")
    return salary

def clean_phone(self):
    phone = self.cleaned_data["phone"]
    if not phone.isdigit() != 10:
        raise forms.ValidationError("phone number must exactly 10 digits")
    return phone

def clean_join_date(self):
    joining_date = self.clean_data['joining_date']
    if joining_date > date.today():
        raise forms.ValidationError("joining cannot be future date")
    return joining_date
        
    
        
