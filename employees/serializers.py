from rest_framework import serializers
from .models import Employee, EmployeeDocument


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee

        fields = [
            "employee_id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "department",
            "designation",
            "salary",
            "joining_date",
            "is_active",
        ]
        
class EmployeeDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDocument
        
        fields = [
            "id",
            "employee",
            "document_name",
            "document_type",
            "file",
            "uploaded_at",
        ]
        read_only_fields = [
            "uploaded_at",
        ]