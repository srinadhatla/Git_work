# Enterprise HRMS Backend System [21]

## Project Overview

Enterprise HRMS Backend System is a production-style Human Resource Management System (HRMS) developed using **Python**, **Django**, **Django REST Framework**, and **PostgreSQL**. The application follows enterprise backend architecture with modular applications, secure REST APIs, role-based access control, reusable business logic, validations, reporting, and comprehensive documentation.

The project is designed to automate core HR operations such as employee management, attendance tracking, leave management, payroll processing, document management, reporting, audit logging, and dashboard analytics.

---

# Technology Stack

* Python 3.12+
* Django
* Django REST Framework (DRF)
* PostgreSQL
* JWT Authentication (Simple JWT)
* ReportLab
* OpenPyXL
* QRCode
* Pillow
* Django Filter
* drf-yasg (Swagger/OpenAPI)

---

# Features

### Authentication

* User Registration
* JWT Login
* Refresh Token
* Logout
* Change Password
* Token Blacklisting
* Role-Based Authentication

### Employee Management

* Employee CRUD Operations
* Employee Profile Management
* Department Mapping
* Search
* Filtering
* Ordering
* Pagination

### Department Management

* Department CRUD
* Department Manager
* Department Statistics
* Employee Count

### Attendance Management

* Mark Attendance
* Check-In / Check-Out
* Daily Attendance
* Monthly Attendance Reports
* Attendance Status
* One Attendance Record Per Day Validation

### Leave Management

* Apply Leave
* Manager Approval Workflow
* HR Approval Workflow
* Leave Rejection
* Leave Tracking
* Leave Status Management

### Payroll

* Payroll Management
* Salary Calculation
* Allowances
* Deductions
* Net Salary
* Salary Slip PDF Generation

### Document Management

* Resume Upload
* Aadhaar Upload
* PAN Upload
* Certificate Upload
* Secure File Management

### Reports

* Employee Reports
* Department Reports
* Attendance Reports
* Payroll Reports
* PDF Export
* Excel Export
* CSV Export

### Dashboard

* Total Employees
* Total Departments
* Today's Attendance
* Pending Leave Requests
* Monthly Payroll Summary
* Recent Employees

### Audit Logs

* User Login
* Logout
* Employee CRUD Logs
* Leave Approval Logs
* Payroll Generation Logs

---

# Project Structure

```text
enterprise_hrms/

├── accounts/
├── employees/
├── departments/
├── attendance/
├── leave_management/
├── payroll/
├── documents/
├── reports/
├── audit_logs/
├── notifications/
├── dashboard/
├── api/
│   ├── serializers.py
│   ├── permissions.py
│   ├── pagination.py
│   ├── filters.py
│   ├── validators.py
│   ├── responses.py
│   ├── exceptions.py
│   └── urls.py
│
├── config/
├── tests/
├── fixtures/
├── media/
├── requirements.txt
├── README.md
└── manage.py
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd enterprise_hrms
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# PostgreSQL Database Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE enterprise_hrms;
```

Create a database user:

```sql
CREATE USER hrms_admin WITH PASSWORD 'password123';

GRANT ALL PRIVILEGES ON DATABASE enterprise_hrms TO hrms_admin;
```

Update `config/settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "enterprise_hrms",
        "USER": "hrms_admin",
        "PASSWORD": "password123",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

---

# Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# Create Superuser

```bash
python manage.py createsuperuser
```

---

# Run Development Server

```bash
python manage.py runserver
```

Application URL:

```
http://127.0.0.1:8000/
```

---

# REST API Base URL

```
http://127.0.0.1:8000/api/v1/
```

---

# Authentication APIs

| Method | Endpoint                      |
| ------ | ----------------------------- |
| POST   | /api/v1/auth/register/        |
| POST   | /api/v1/auth/login/           |
| POST   | /api/v1/auth/refresh/         |
| POST   | /api/v1/auth/logout/          |
| POST   | /api/v1/auth/change-password/ |

---

# Department APIs

| Method | Endpoint                  |
| ------ | ------------------------- |
| GET    | /api/v1/departments/      |
| POST   | /api/v1/departments/      |
| GET    | /api/v1/departments/{id}/ |
| PUT    | /api/v1/departments/{id}/ |
| DELETE | /api/v1/departments/{id}/ |

---

# Employee APIs

| Method | Endpoint                |
| ------ | ----------------------- |
| GET    | /api/v1/employees/      |
| POST   | /api/v1/employees/      |
| GET    | /api/v1/employees/{id}/ |
| PUT    | /api/v1/employees/{id}/ |
| PATCH  | /api/v1/employees/{id}/ |
| DELETE | /api/v1/employees/{id}/ |

Supports:

* Search
* Filter
* Ordering
* Pagination

---

# Attendance APIs

| Method | Endpoint                 |
| ------ | ------------------------ |
| GET    | /api/v1/attendance/      |
| POST   | /api/v1/attendance/      |
| GET    | /api/v1/attendance/{id}/ |
| PUT    | /api/v1/attendance/{id}/ |
| DELETE | /api/v1/attendance/{id}/ |

Supports:

* Monthly Attendance
* Employee Attendance
* Attendance Status
* Search
* Filter
* Ordering
* Pagination

---

# Leave Management APIs

| Method | Endpoint                             |
| ------ | ------------------------------------ |
| GET    | /api/v1/leaves/                      |
| POST   | /api/v1/leaves/                      |
| GET    | /api/v1/leaves/{id}/                 |
| PUT    | /api/v1/leaves/{id}/                 |
| DELETE | /api/v1/leaves/{id}/                 |
| POST   | /api/v1/leaves/{id}/manager_approve/ |
| POST   | /api/v1/leaves/{id}/hr_approve/      |
| POST   | /api/v1/leaves/{id}/reject/          |

---

# Security Features

* JWT Authentication
* Refresh Tokens
* Password Validation
* Role-Based Access Control (RBAC)
* Object-Level Permissions
* Secure File Upload
* Input Validation
* Token Blacklisting

---

# Business Validations

### Employee

* Unique Employee ID
* Unique Email
* Unique Phone Number

### Attendance

* One Attendance Record Per Employee Per Day
* Check-Out Time Must Be After Check-In Time

### Leave

* Start Date Must Be Before End Date

### Payroll

* Salary Must Be Greater Than Zero

---

# Future Modules

The following modules will be added during the next implementation phases:

* Payroll APIs
* Salary Slip PDF Generation
* Document Management
* Dashboard APIs
* Reports (PDF, Excel, CSV)
* Notifications
* Audit Logging
* Swagger/OpenAPI Documentation
* Automated Testing
* 90% Code Coverage
* Postman Collection
* SQL Database Dump
* ER Diagram

---

# Testing

Run all tests:

```bash
python manage.py test
```

Generate coverage report:

```bash
coverage run manage.py test
coverage report
```

Target Coverage:

```
90%
```

---

# Git Workflow

```bash
git checkout development

git pull origin development

git checkout -b epic/hrms-backend-phase1
```

Example commit messages:

```bash
git commit -m "feat: implement employee management module"

git commit -m "feat: implement attendance module"

git commit -m "feat: implement leave management"

git commit -m "feat: implement payroll module"

git commit -m "docs: update README"
```

---

# Deliverables

* Enterprise HRMS Backend Source Code
* PostgreSQL Database Schema
* REST APIs
* JWT Authentication
* Department Management
* Employee Management
* Attendance Management
* Leave Management
* Payroll Module
* Document Management
* Dashboard APIs
* Reporting Module
* Swagger Documentation
* Postman Collection
* SQL Dump
* ER Diagram
* README Documentation
* Automated Tests
* Coverage Report

---

# Author

**Atla Srinadh Reddy**

Python Backend Developer
