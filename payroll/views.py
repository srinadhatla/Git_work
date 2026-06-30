from django.db import connection
import time

from rest_framework.decorators import api_view
from rest_framework.response import Response

from payroll.models import Payroll

@api_view(["GET"])
def payroll_report(request):
    connection.queries.clear()
    start = time.time()
    payrolls = Payroll.objects.select_related("employee")
    list(payrolls)
    end = time.time()
    print("Queries:", len(connection.queries))
    print("Response Time:", end-start)
    return Response({"count": payrolls.count()})