from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Employee
from departments.models import Department
from .forms import EmployeeForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import EmployeeSerializer

from django.shortcuts import get_object_or_404

from rest_framework.views import APIView

from rest_framework.viewsets import ModelViewSet

from rest_framework import generics

from rest_framework.permissions import IsAuthenticated

from .permissions import (ReadOnlyPermission,IsAdmin,IsHR)

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .pagination import EmployeePagination

from employees.services.employee_service import EmployeeService

from employees.responses.api_response import (success_response,error_response) 

from core.responses import (SuccessResponse,ErrorResponse)

from .throttles import EmployeeThrottle


from rest_framework.decorators import api_view
from employees.throttles import LoginThrottle

from rest_framework.decorators import throttle_classes

from django.views.decorators.cache import cache_page

from django.shortcuts import get_object_or_404

from rest_framework import status

import time
from django.db import connection

from django.db import transaction

from rest_framework.response import Response

from employees.services.employee_service import SalaryService

from django.db.models import Count, Avg

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

    departments = Department.objects.prefetch_related("employee_set").all()
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
    employee = get_object_or_404(Employee,id=pk)

    if request.method == 'POST':
        form = EmployeeForm(request.POST,request.FILES,instance=employee)

        if form.is_valid():
            form.save()
            return redirect('employee_list')

    else:
        form = EmployeeForm(instance=employee)

    return render(request,'employees/update.html',{'form': form})

def delete_employee(request, pk):
    employee = get_object_or_404(Employee,id=pk)

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
    employee = get_object_or_404(Employee.objects.select_related("department"),id=id)
    return render(request, 'employees/employee_detail.html', {'employee': employee})


@api_view(['GET'])
@cache_page(60 * 5)
def employee_list_api(request):
    employees = Employee.objects.select_related('department').all()
    departments = Department.objects.prefetch_related("employee_set").all()
    serializer = EmployeeSerializer(employees,many=True)
    return success_response("Employees fetched successfully",serializer.data)


@api_view(['GET'])
def employee_detail_api(request, id):
    try:
        employee = Employee.objects.select_related("department").get(id=id)

    except Employee.DoesNotExist:

        return Response(
            {"error": "Employee not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    connection.queries.clear()
    start=time.time()
    employee=Employee.objects.select_related("department").get(id=id)
    end=time.time()
    print("Queries:",len(connection.queries))
    print("Response Time:",end-start)
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data)

@api_view(['POST'])
def employee_create_api(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():   
        with transaction.atomic():
            employee = serializer.save()
        return success_response(message="Employee Created Successfully",data=serializer.data,status=201)
    return error_response(message="Validation Failed",errors=serializer.errors)


@api_view(['PUT'])
def employee_update_api(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"},status=status.HTTP_404_NOT_FOUND)
    serializer = EmployeeSerializer(employee,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def employee_delete_api(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"},status=status.HTTP_404_NOT_FOUND)
    employee.delete()
    return Response({"message": "Employee deleted"},status=status.HTTP_200_OK)


@api_view(['POST'])
def process_salary_api(request):
    employee_id = request.data['employee_id']
    increment = request.data['increment']
    result = SalaryService.process_salary(
        employee_id=employee_id,
        increment_amount=increment,
        user=request.user.username if request.user else None
    )
    return Response({
        "message": "Salary processed successfully",
        "data": result
    })
    
@api_view(['POST'])
@api_view(['POST'])
def process_salary_api(request):
    employee_id = request.data['employee_id']
    increment = request.data['increment']
    result = SalaryService.process_salary(
        employee_id=employee_id,
        increment_amount=increment,
        user=request.user.username if request.user else None
    )
    return Response({
        "message": "Salary processed successfully",
        "data": result
    })


@api_view(['GET'])
def department_report(request):
    connection.queries.clear()
    start = time.time()
    report = Department.objects.prefetch_related("employee_set").annotate(total_employees=Count("employee"),average_salary=Avg("employee__salary"))
    data = report.values("name","total_employees","average_salary")
    list(report)
    end = time.time()
    print("Queries:", len(connection.queries))
    print("Response Time:", end-start)
    return Response(data)


    
@api_view(['GET'])
def employee_salary_report(request):
    data = Employee.objects.values(
        "employee_id",
        "first_name",
        "salary"
    )

    return Response(data)

@api_view(['GET'])
def employee_salary_list(request):
    data = Employee.objects.values_list(
        "employee_id",
        "salary"
    )

    return Response(data)

from django.db.models import Count, Avg

@api_view(['GET'])
def department_summary(request):

    data = Department.objects.annotate(
        total_employees=Count("employee"),
        avg_salary=Avg("employee__salary")
    ).values(
        "name",
        "total_employees",
        "avg_salary"
    )

    return Response(data)

from django.db.models import Avg, Sum

@api_view(['GET'])
def company_salary_summary(request):

    data = Employee.objects.aggregate(
        avg_salary=Avg("salary"),
        total_salary=Sum("salary")
    )

    return Response(data)

class EmployeeAPIView(APIView):
    def get(self, request):
        employees = Employee.objects.select_related("department").all()
        serializer = EmployeeSerializer(employees,many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class EmployeeListAPIView(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    def get_queryset(self):
        connection.queries.clear()
        start = time.time()
        queryset = Employee.objects.select_related("department")
        list(queryset)
        end = time.time()
        print("Queries:", len(connection.queries))
        print("Response Time:", end-start)
        return queryset
    
class EmployeeRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Employee.objects.select_related("department")
    serializer_class = EmployeeSerializer
    
class EmployeeCreateAPIView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class EmployeeUpdateAPIView(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    
class EmployeeDeleteAPIView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated,IsAdmin]
    

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.select_related('department')
    serializer_class = EmployeeSerializer
    pagination_class = EmployeePagination
    throttle_classes = [EmployeeThrottle]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    permission_classes = [IsAuthenticated,IsAdmin]
    search_fields = ['employee_id','first_name','email']
    filterset_fields = ['department','status','designation']
    ordering_fields = ['salary','joining_date']
    

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.select_related("department")
    serializer_class = EmployeeSerializer
    permission_classes = [ReadOnlyPermission]
    
class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.select_related("department")
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    
    
class EmployeeCreateView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    
