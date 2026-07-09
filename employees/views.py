from django.shortcuts import render
from django.db.models import Count, Max, Min, Avg

from django.utils import timezone

from employees.models import Employee, Department

from django.core.cache import cache

today = timezone.now().date()

from django.core.paginator import Paginator

from django.db.models import Q

from employees.services.dashboard_service import get_dashboard_statistics

from django.core.cache import cache

from employees.services.employee_service import (get_paginated_employees,search_employees,)

from employees.services.dashboard_service import (get_dashboard_statistics,)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import EmployeeDocument
from .serializers import EmployeeDocumentSerializer

import os
from django.http import response
from django.conf import settings

from rest_framework.permissions import IsAuthenticated

from .permissions import IsHRorAdmin, IsDocumentOwnerOrHR

from .csv_handler import (import_csv,export_csv)

from .excel_import import import_employees

from django.http import HttpResponse

from .excel_export import export_employees

from .pdf_generator import generate_employee_profile_pdf

def dashboard(request):
    dashboard_data = cache.get("dashboard_data")
    if not dashboard_data:
        dashboard_data = get_dashboard_statistics()
        cache.set("dashboard_data",dashboard_data,timeout=120,)
    return render(request, "dashboard.html", dashboard_data)


def employee_list(request):
    employees = cache.get("employees_list")

    if employees is None:
        employees = list(
            Employee.objects.select_related("department").only(
                "id",
                "employee_id",
                "first_name",
                "last_name",
                "department__name",
                "salary",
            )
        )
        cache.set("employees_list", employees, timeout=300)

    paginator = Paginator(employees, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "employees/employees_list.html", {"page_obj": page_obj})

def employee_search(request):
    query = request.GET.get("q", "")
    department = request.GET.get("department", "")
    status = request.GET.get("status", "")
    employees = search_employees(query,department,status,)
    return render(request,"employees/employee_search.html",
        {
            "employees": employees,
            "query": query,
            "department": department,
            "status": status,
        },
    )
    
def department_list(request):
    departments = cache.get("departments")
    if departments is None:
        departments = Department.objects.prefetch_related("employee_set")
        cache.set("departments", departments, timeout=1800)

    paginator = Paginator(departments, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "employees/departments_list.html", {"page_obj": page_obj})


class DocumentUploadAPIView(APIView):
    permission_classes = [IsAuthenticated,IsHRorAdmin]
    def post(self, request, id):
        serializer = EmployeeDocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Document uploaded successfully",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class DocumentListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if (user.is_staff or user.groups.filter(name="HR").exists()):
            documents = EmployeeDocument.objects.all()
        else:
            documents = EmployeeDocument.objects.filter(employee__user=user)


        serializer = EmployeeDocumentSerializer(documents,many=True)
        return Response(serializer.data)        
    
class DocumentDownloadAPIView(APIView):
    permission_classes = [IsAuthenticated,IsDocumentOwnerOrHR]
    def get(self, get, id):
        try:
            document = EmployeeDocument.objects.get(id=id)
        except EmployeeDocument.DoesNotExist:
            return Response(
                {
                    "error": "Document not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
            response = FileResponse(open(file_path, 'rb'),as_attachment=True,filename=document.file.name.split('/')[-1])
            return response
        
class DocumentDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated,IsHRorAdmin]
    def post(self, request, id):
        try:
            document = EmployeeDocument.objects.get(id=id)
        except EmployeeDocument.DoesNotExist:
            return Response({"error": "Document not found"},status=status.HTTP_404_NOT_FOUND)
            
        if document.file:
            if os.path.exists(document.file.path):
                os.remove(document.file.path)
            document.delete()
            return Response({"message": "Document Delete succcessfully"},status=status.HTTP_200_OK)
            
class EmployeeExcelImportAPIView(APIView):
    permission_classes = [IsAuthenticated,IsHRorAdmin]
    def post(self, request):
        file = request.FILES.get("file")

        if not file:
            return Response({"error":"Excel file required"},status=400)
        result = import_employees(file)
        
        return Response(result,status=201)
            
class EmployeeCSVImportAPIView(APIView):
    permission_classes = [IsAuthenticated,IsHRorAdmin]
    def post(self, request):
        file = request.FILES.get("file")

        if not file:
            return Response({"error":"CSV file required"},status=400)
        result = import_csv(file)

        return Response(result)
    
class EmployeeExcelExportAPIView(APIView):
    permission_classes = [IsAuthenticated,IsHRorAdmin]

    def get(self, request):
        file = export_employees()
        response = HttpResponse(file,content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response["Content-Disposition"] = ('attachment; filename="employees.xlsx"')
        return response

class EmployeeCSVImportAPIView(APIView):
    permission_classes = [IsAuthenticated,IsHRorAdmin]

    def post(self, request):
        file = request.FILES.get("file")

        if not file:
            return Response({"error":"CSV file required"},status=400)
        result = import_csv(file)
        return Response(result)
    
class EmployeeCSVExportAPIView(APIView):
    permission_classes = [IsAuthenticated,IsHRorAdmin]

    def get(self, request):
        csv_file = export_csv()
        response = HttpResponse(csv_file,content_type="text/csv")

        response["Content-Disposition"] = ('attachment; filename="employees.csv"')
        return response
    
class EmployeeProfilePDFAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        
        try:
            employee = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            return Response(
                {
                    "error": "Employee Not Found"
                },status=404
            )
        pdf = generate_employee_profile_pdf(employee)
        response = HttpResponse(pdf, content_type="application/pdf")
        
        response["Content-Disposition"] = (f'attachment; filename="{employee.employee_id}_profile.pdf"')