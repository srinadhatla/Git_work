# 🚀 Employee Management API System (Django REST Framework)

A complete **REST API-based Employee Management System** built using Django REST Framework (DRF) with JWT authentication, RBAC, filtering, pagination, and API documentation.

---

## 📌 Project Overview

This project demonstrates a full backend API system for HRMS including:

- REST API design principles
- Django REST Framework implementation
- JWT Authentication
- Role-Based Access Control (RBAC)
- CRUD operations for Employees & Departments
- Filtering, Searching & Ordering
- Pagination
- Swagger API Documentation

---

## 🌐 Module 1: Introduction to REST APIs

### What is REST?
REST (Representational State Transfer) is an architecture used for communication between client and server.

### Examples:
- React ↔ Django API
- Flutter ↔ Backend API
- Mobile Apps ↔ Server

### REST Principles:
- Stateless communication
- Client-Server architecture
- Resource-based URLs
- JSON responses
- Standard HTTP methods (GET, POST, PUT, DELETE)

---

## ⚙️ Module 2: Django REST Framework Setup

### Installation
```bash
pip install djangorestframework
pip install djangorestframework-simplejwt


settings.py
INSTALLED_APPS = [
    "rest_framework",
]

🔄 Module 3: Serializers
What is a Serializer?

Converts:

Django Model → JSON
JSON → Django Model
Example
from rest_framework import serializers
from employees.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
📡 Module 4: Function-Based APIs
Example
@api_view(['GET'])
def employee_list(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)
APIs to implement:
GET /api/employees/
GET /api/employees/{id}/
POST /api/employees/
PUT /api/employees/{id}/
DELETE /api/employees/{id}/
🧩 Module 5: Class-Based APIs

Use APIView for structured API handling:

GET
POST
PUT
DELETE
⚡ Module 6: Generic Views
Learn:
ListAPIView
RetrieveAPIView
CreateAPIView
UpdateAPIView
DestroyAPIView
Benefit:
Less code
Faster development
Clean architecture
🔁 Module 7: ViewSets & Routers
Example
from rest_framework.viewsets import ModelViewSet

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
Router
router.register('employees', EmployeeViewSet)
🔐 Module 8: JWT Authentication
Setup
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
APIs
POST /api/token/
POST /api/token/refresh/
Response Example
{
    "access": "jwt_token",
    "refresh": "refresh_token"
}
🛡️ Module 9: Permissions (RBAC)
Roles:
Admin → Full access
HR → Create & update employees
Employee → View own profile
Permissions:
IsAuthenticated
IsAdminUser
Custom permissions
🔎 Module 10: Filtering, Searching & Ordering
Install
pip install django-filter
Features:
Search: name, email, employee_id
Filter: department, status, designation
Ordering: salary, joining_date
Example
/api/employees/?search=ajay
/api/employees/?department=IT
/api/employees/?ordering=-salary
📄 Module 11: Pagination
PageNumberPagination
10 records per page
📚 Module 12: API Documentation
Install Swagger
pip install drf-yasg
URLs
/swagger/
/redoc/
🏗️ Project Structure
company_portal/
│
├── api/
│   ├── serializers.py
│   ├── permissions.py
│   ├── pagination.py
│   ├── filters.py
│   ├── views.py
│   ├── urls.py
│
├── accounts/
├── employees/
├── departments/
│
└── requirements.txt
🧠 Company-Level Assignment

Build a complete backend system:

🔐 Authentication APIs
Login
Token refresh
👨‍💼 Employee APIs
CRUD operations
Search / Filter / Pagination
🏢 Department APIs
CRUD operations
👤 User APIs
Profile management
📘 API Documentation
Swagger
Redoc
🔐 Security
JWT Authentication
Role-Based Access Control
🚀 Tech Stack
Python
Django
Django REST Framework
SimpleJWT
Django Filter
drf-yasg (Swagger)
👨‍💻 Author

Srinadh Reddy Atla
GitHub: https://github.com/srinadhatla
