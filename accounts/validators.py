import os

import re

from django.core.exceptions import ValidationError

from rest_framework import serializers

from datetime import date

ALLOWED_EXTENSIONS = [".jpg",".png",".jpeg"]
MAX_FILE_SIZE = 2 * 1024 * 1024

def validate_profile_image(image):
    extension = os.path.splitext(image.name)[1].lower()
    
    if extension not in ALLOWED_EXTENSIONS:
        raise ValidationError("Only jpeg, jpg and png are allowed")
    
    if image.size > MAX_FILE_SIZE:
        raise ValidationError("image size must not exceed 2mb")
    
    if image.content not in ["image/jpeg","image/png"]:
        raise ValidationError("Invalid Image MIME type")
    
def validate_employee_id(value):
    pattern = r"^EMP\d{5}$"
    if not re.match(pattern, value):
        raise serializers.ValidationError("Employee ID must in the format of EMP0001.")
    return value

def validate_email(value):
    from employees.models import Employee
    if Employee.objects.filter(email=value).exists():
        raise serializers.ValidationError("Email already exists")
    return value

def validate_phone(value):
    if not value.isdigit() or len(value) != 10:
        raise serializers.ValidationError("Phone number digits must contain 10.")
    
def validate_salary(value):
    if value<=0:
        raise serializers.ValidationError("Salary must be greater then zero.")
    return value

def validate_joining_date(self, value):
    if value > date.today():
        raise serializers.ValidationError("Joining date cannot be in future date.")
    return value