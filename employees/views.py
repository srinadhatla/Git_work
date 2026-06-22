from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Employee
from departments.models import Department
from .forms import EmployeeForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator




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
    designation = request.GET.get('designation')
    status = request.GET.get('status')
    employees = Employee.objects.all()
    print(employees)
    print(department_id)
    if search:
        employees = employees.filter(
            Q(employee_id__icontains=search) |
            Q(first_name__icontains=search) |
            Q(email__icontains=search) |
            Q(department__name__icontains=search)
        )

    if department_id:
        employees = employees.filter(department_id=department_id)
        
    if designation:
        employees = employees.filter(designation=designation)
        
    if status:
        employees = employees.filter(status = status)
        
    paginator = Paginator(employees, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    departments = Department.objects.all()
    print(employees)
    return render(request,'employees/list.html',{'employees': employees,'page_obj': page_obj,'departments':departments,'search':search,'department_id':department_id,'designation':designation,'status':status})


def add_employee(request):

    departments = Department.objects.all()

    if request.method == "POST":

        Employee.objects.create(
            employee_id=request.POST['employee_id'],
            first_name=request.POST['first_name'],
            email=request.POST['email'],
            salary=request.POST['salary'],
            department_id=request.POST['department'],
            profile_image=request.FILES.get('profile_image'),
        )

        return redirect('employee_list')

    return render(request,'employees/add.html',{'departments': departments})



def update_employee(request, pk):
    employee = Employee.objects.get(id=pk)

    if request.method == 'POST':
        form = EmployeeForm(request.POST,request.FILES,instance=employee)

        if form.is_valid():
            form.save()
            return redirect('employee_list')

    else:
        form = EmployeeForm(instance=employee)

    return render(request,'employees/update.html',{'form': form})

def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)

    if employee.profile_image:
        employee.profile_image.delete()
        employee.save()

    return redirect('employee_detail', id=pk)

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