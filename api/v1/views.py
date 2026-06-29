from rest_framework.decorators import api_view
from rest_framework.response import Response

from employees.models import Employee
from core.responses import SuccessResponse
from .serializers import EmployeeV1Serializer

@api_view(['GET'])
def employee_list(request):
    employees = Employee.objects.all()
    serializer = EmployeeV1Serializer(employees,many=True)
    return SuccessResponse(message="V1 Employees",data=serializer.data)