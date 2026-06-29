from django.shortcuts import render, redirect, get_object_or_404
from .models import Department

from rest_framework.viewsets import ModelViewSet

from .serializers import DepartmentSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.views.decorators.cache import cache_page

import time
from django.db import connection


@api_view(['GET'])
@cache_page(60 * 5)
def department_list_api(request):
    start_time = time.time()
    departments = Department.objects.prefetch_related('employee_set')
    serializer = DepartmentSerializer(departments,many=True)
    print("Query Count:",len(connection.queries))
    print("Response Time:",time.time() - start_time)
    return Response(serializer.data)


def add_department(request):
    if request.method == "POST":
        Department.objects.create(
            name=request.POST['name'],
            description=request.POST['description']
        )
        return redirect('department_list')

    return render(request, 'departments/add.html')


def update_department(request, id):
    department = get_object_or_404(Department, id=id)

    if request.method == "POST":
        department.name = request.POST['name']
        department.description = request.POST['description']
        department.save()
        return redirect('department_list')

    return render(request, 'departments/update.html',{'department': department})


def delete_department(request, id):
    department = get_object_or_404(Department, id=id)
    department.delete()

    return redirect('department_list')

class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.prefetch_related('employee_set')
    serializer_class = DepartmentSerializer 