from rest_framework.decorators import api_view

from employees.models import Employee
from core.responses import SuccessResponse
from .serializers import EmployeeV2Serializer


@api_view(['GET'])
def employee_list(request):
    employees = Employee.objects.all()
    serializer = EmployeeV2Serializer(employees,many=True)
    return SuccessResponse(message="V2 Employees",data=serializer.data)