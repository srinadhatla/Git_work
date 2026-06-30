from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import (admin_required,hr_required,manager_required)
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.views import PasswordChangeView


from .forms import RegistrationForm, LoginForm
from .models import UserProfile

from employees.models import Employee
from departments.models import Department

from  django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from django.http import HttpResponse

from .forms import ProfileUpdateForm

from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer

from audit_logs.models import AuditLog

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            UserProfile.objects.create(
                user=user,
                employee_id=form.cleaned_data['employee_id'],
                role=form.cleaned_data['role'],
                phone=form.cleaned_data['phone'],
            )
            messages.success(request, "Registration successful")
            return redirect('login')
        else:
            form = RegistrationForm()
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                AuditLog.objects.create(
                    user=user.username,
                    action="LOGIN",
                    module="Authentication",
                    ip_address=request.META.get('REMOTE_ADDR')
                )
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid credentials")
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})
    
    
def logout_view(request):
    AuditLog.objects.create(
        user=request.user.username,
        action="LOGOUT",
        module="Authentication",
        ip_address=request.META.get('REMOTE_ADDR')
    )
    logout(request)
    return redirect('login')
    
    

@permission_required('employees.delete_employee')
@admin_required
def delete_employee(request):
    return render(request,'accounts/delete_employee.html')  


@permission_required('employees.add_employee')
@admin_required
@hr_required
def add_employee(request):
    return render(request,'accounts/add_employee.html')

@admin_required
@hr_required
def update_employee(request):
    return render(request,'accounts/update_employee.html')

@admin_required
@hr_required
@manager_required
def view_reports(request):
    return render(request,'accounts/view_reports.html')

@admin_required
@hr_required
@manager_required
def view_own_profile(request):
    return render(request,'accounts/view_own_profile.html')


def profile(request):
    return render(request,'accounts/profile.html')


def profile(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile': profile})

@login_required
def dashboard(request):
    profile = UserProfile.objects.get(user=request.user)

    if profile.role == "ADMIN":
        return redirect('admin_dashboard')

    elif profile.role == "HR":
        return redirect('hr_dashboard')

    elif profile.role == "EMPLOYEE":
        return redirect('employee_dashboard')
    
    elif profile.role == "manager":
        return redirect("manager_dashboard")

    return render(request, 'accounts/dashboard.html')


@login_required
def admin_dashboard(request):
    context = {
        'total_employees': Employee.objects.count(),
        'total_departments': Department.objects.count(),
        'total_users': User.objects.count(),
    }

    return render(request,'accounts/admin_dashboard.html',context)

@login_required
def hr_dashboard(request):
    context = {'total_employees': Employee.objects.count(),}
    return render(request,'accounts/hr_dashboard.html',context)

@login_required
def employee_dashboard(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request,'accounts/employee_dashboard.html',{'profile': profile})


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('login')


def verify_email(request, user_id):
    profile = UserProfile.objects.get(user_id=user_id)
    profile.is_email_verified = True
    profile.save()
    return HttpResponse("Email verified successfully")

from .forms import ProfileUpdateForm

@login_required
def update_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile updated successfully")
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request,'accounts/update_profile.html',{'form': form})

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
