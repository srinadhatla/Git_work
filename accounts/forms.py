from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
import re


class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    phone = forms.CharField(max_length=15, required=True)
    employee_id = forms.CharField(max_length=20, required=True)
    role = forms.ChoiceField(choices=UserProfile.ROLE_CHOICES, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)
    
    
    
def clean_email(self):
    email = self.cleaned_data.get('email')
    if User.objects.filter(email=email).exists():
        raise forms.ValidationError("Email already exists")
    return email


def clean_employee_id(self):
    employee_id = self.cleaned_data.get('employee_id')
    if not employee_id.startswith('EMP'):
        raise forms.ValidationError("Employee ID must start with 'EMP'")
    if UserProfile.objects.filter(employee_id=employee_id).exists():
        raise forms.ValidationError("Employee_id already exists")
    return employee_id

def clean_password(self):
    password = self.cleaned_data.get('password')
    pattern = (
        r'^(?=.*[a-z])'
        r'^(?=.*[A-Z])'
        r'^(?=.*\d)'
        r'^(?=.*[@$!%*?&])'
        r'^([A-Za-z\d@$!%*?&])'
        r'^{8,}$'
    )
    
    if not re.match(pattern, password):
        raise forms.ValidationError("Password must be Minimum 8 characters long", "contain at least one uppercase letter", "contain at least one uppercase letter", "atleast one number and one specia character")
    return password



def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data.get('password')
    confirm = cleaned_data.get('confirm_password')
    if password != confirm:
        raise forms.ValidationError("Passwords do not match")
    return cleaned_data

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
    


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile 
        fields = ['profile_image','phone','designation','department']