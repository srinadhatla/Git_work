from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from accounts.validators import validate_profile_image

from .validators import validate_file_size, validate_image_extension, validate_pdf_extension

class Department(models.Model):
    name = models.CharField(max_length=100,unique=True, db_index=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    employee_id = models.CharField(max_length=20,unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, db_index=True)
    phone = models.CharField(max_length=15)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL,related_name="employees",null=True,blank=True)
    designation = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField(db_index=True)
    is_active = models.BooleanField(default=True, db_index=True)
    previous_salary = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    previous_department = models.CharField(max_length=100,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(upload_to="profile_images/",validators=[validate_profile_image],blank=True,null=True)
    profile_photo = models.ImageField(upload_to="employees/profile_photos/",validators=[validate_file_size,validate_image_extension],null=True,blank=True)
    resume = models.FileField(upload_to="employees/resumes/",validators=[validate_file_size,validate_pdf_extension],null=True,blank=True)
    aadhaar_document = models.FileField(upload_to="employees/documents/aadhaar/",validators=[validate_file_size,validate_pdf_extension],null=True,blank=True)
    pan_document = models.FileField(upload_to="employees/documents/pan/",validators=[validate_file_size,validate_pdf_extension],null=True,blank=True)
    
    
    
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def clean(self):
        if self.salary<0:
            raise ValidationError({"salary": "salary cannot be negative."})
        if self.joining_date>timezone.now().date():
            raise ValidationError({"joining_date": "Joining date cannot be in future"})
    def save(self, *args, **kwargs):
        self.full_clean()
        if self.pk:
            old_employee = Employee.objects.get(pk=self.pk)
            if old_employee.employee_id!=self.employee_id:
                raise ValidationError("Employee ID cannot change after creation.")
        super().save(*args, **kwargs)
        
    class Meta:
        indexes = [
            models.Index(fields=["is_active", "joining_date"]),
            models.Index(fields=["department", "is_active"]),
        ]


class EmployeeProfile(models.Model):
    employee = models.OneToOneField(Employee,on_delete=models.CASCADE)
    address = models.TextField(blank=True)
    emergency_contact = models.CharField(max_length=15, blank=True)
    blood_group = models.CharField(max_length=5, blank=True)
    photo = models.ImageField(upload_to="employees/", blank=True, null=True)
    skills = models.TextField(blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.employee.first_name


class BlockedIP(models.Model):
    ip_address = models.GenericIPAddressField(protocol='both')
    reason = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip_address
    
    
class EmployeeDocument(models.Model):
    DOCUMENT_TYPES = [
        ('resume', 'Resume'),
        ('pan', 'PAN'),
        ('aadhaar', 'Aadhaar'),
        ('degree', 'Degree Certificate'),
        ('experience', 'Experience Certificate'),
        ('offer', 'Offer'),
    ]
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name="documents")
    document_name = models.CharField(max_length=255)
    document_type = models.CharField(max_length=50,choices=DOCUMENT_TYPES)
    file = models.FileField(upload_to="documents/",validators=[validate_file_size,validate_pdf_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.employee} - {self.document_name}"
    
    
    