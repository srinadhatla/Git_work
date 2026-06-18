from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Employee
from departments.models import Department
from .forms import EmployeeForm
from django.contrib import messages



def index(request):
    return render(request, "employees/index.html")
def home(request):
    return render(request, "employees/home.html")
def about(request):
    return render(request, "employees/about.html")
def contact(request):
    return render(request, "employees/contact.html")


def employee_list(request):

    search = request.GET.get('search')
    department_id = request.GET.get('department')

    employees = Employee.objects.all()

    if search:
        employees = employees.filter(first_name__icontains=search)

    if department_id:
        employees = employees.filter(department_id=department_id)

    departments = Department.objects.all()

    return render(request,'employees/list.html',{'employees': employees,'departments': departments})


def add_employee(request):

    departments = Department.objects.all()

    if request.method == "POST":

        Employee.objects.create(
            employee_id=request.POST['employee_id'],
            first_name=request.POST['first_name'],
            email=request.POST['email'],
            salary=request.POST['salary'],
            department_id=request.POST['department']
        )

        return redirect('employee_list')

    return render(request,'employees/add.html',{'departments': departments})


def update_employee(request, id):

    employee = get_object_or_404(Employee, id=id)
    form = EmployeeForm(request.POST or None, request.FILES or None, instance=employee)

    if form.is_valid():
        form.save()
        messages.success(request, "Employee updated successfully")
        return redirect('employee_list')

    return render(request, 'employees/employee_form.html', {'form': form})


def delete_employee(request, id):

    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        employee.delete()
        messages.success(request, "Employee deleted successfully")
        return redirect('employee_list')

    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})


def filter_employee(request, id):
    employees = Employee.objects.filter(department_id=id)
    return render(request, 'employees/list.html', {'employees': employees})
    
    
def create_employee(request):
    form = EmployeeForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save() 
        messages.success(request, "Employee created successfully")
        return redirect('employee_list')

    return render(request, 'employees/employee_form.html', {'form': form})

    
def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)
    return render(request, 'employees/employee_detail.html', {'employee': employee})