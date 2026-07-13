# HRMS Automation System

## Day 19 - File Management, Reporting & Enterprise HR Automation Module

---

# Project Overview

HRMS Automation System is a Django-based Human Resource Management System designed to automate employee management and HR operations within an organization.

The system provides a centralized platform for managing employee information, authentication, employee documents, reports, file processing, audit tracking, and performance monitoring.

This project follows:

**Architecture: Modular Django Architecture with Service Layer Pattern**

The system is designed for enterprise HR operations with support for:

* Employee management
* HR/Admin role management
* Secure authentication
* Document management
* CSV and Excel data processing
* PDF report generation
* Audit logging
* Performance monitoring
* API security

---

# Technology Stack

## Backend

* Python
* Django 6.0.6
* Django REST Framework
* Simple JWT Authentication

## Database

* SQLite3

## File Processing

* CSV Processing
* Excel Processing
* PDF Generation

## Libraries

* djangorestframework
* djangorestframework-simplejwt
* openpyxl
* Pillow
* ReportLab
* PyJWT

---

# Installed Packages

```
asgiref==3.11.1
charset-normalizer==3.4.9
colorama==0.4.6
Django==6.0.6
djangorestframework==3.17.1
djangorestframework_simplejwt==5.5.1
et_xmlfile==2.0.0
openpyxl==3.1.5
pillow==12.2.0
PyJWT==2.13.0
qrcode==8.2
reportlab==5.0.0
sqlparse==0.5.5
tzdata==2026.2
```

---

# Project Architecture

## Modular Django Architecture with Service Layer Pattern

The project follows a modular application structure.

## Applications

### accounts

Responsible for:

* User authentication
* JWT token generation
* Password management
* Permissions
* Security handling

### employees

Responsible for:

* Employee management
* Department management
* Employee documents
* CSV import/export
* Excel import/export
* PDF generation
* Employee services

### audit_logs

Responsible for:

* Tracking user activities
* Employee activity records
* System audit history

### logs

Responsible for:

* Application logs
* Error logs
* Security logs
* Performance logs

---

# Project Structure

```
HRMS Automation System

├── accounts
│   ├── authentication.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── security.py
│   ├── throttles.py
│   └── views.py
│
├── employees
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── signals.py
│   ├── csv_handler.py
│   ├── excel_import.py
│   ├── excel_export.py
│   ├── pdf_generator.py
│   │
│   └── services
│       ├── employee_service.py
│       ├── dashboard_service.py
│       └── report_service.py
│
├── audit_logs
│
├── logs
│
├── company_portal
│   ├── settings.py
│   ├── urls.py
│   └── middleware.py
│
├── reports
│
├── templates
│
├── manage.py
└── requirements.txt
```

---

# Employee Management Module

Features implemented:

* Employee creation
* Employee update
* Employee listing
* Employee search
* Department management
* Pagination
* Active/inactive employee tracking

Employee details include:

* Employee ID
* First Name
* Last Name
* Email
* Phone
* Department
* Designation
* Salary
* Joining Date
* Profile Images

Employee history tracking:

* Previous salary
* Previous department

---

# File Management Module

The system provides employee document management.

## Supported Documents

* Resume
* PAN Document
* Aadhaar Document
* Degree Certificate
* Experience Certificate
* Offer Letter

## File Operations

Implemented:

* Document upload
* Document listing
* Document download
* Document deletion

## File Validation

Implemented validations:

* File size validation
* Image extension validation
* PDF extension validation

---

# CSV Import & Export

Implemented CSV operations:

## CSV Import

Features:

* Header validation
* Duplicate email checking
* Department creation
* Error handling

## CSV Export

Exports employee details:

* Employee ID
* Name
* Email
* Phone
* Department
* Designation
* Salary
* Joining Date

---

# Excel Import & Export

Implemented Excel processing using OpenPyXL.

Features:

* Excel employee import
* Excel employee export
* Data validation
* Duplicate checking
* Error reporting

---

# PDF Report Generation

Implemented employee profile PDF generation using ReportLab.

Generated PDF contains:

* Employee ID
* Employee name
* Email
* Phone
* Department
* Designation
* Salary
* Joining Date

---

# Authentication & Security

Implemented JWT authentication using Django REST Framework Simple JWT.

## Authentication Features

* User login
* Access token generation
* Refresh token generation
* Logout
* Token blacklist
* Change password
* Forgot password
* Reset password

---

# Role Based Access Control

Implemented custom permissions for:

* Admin
* HR
* Manager
* Employee

Custom permission classes:

* IsAdmin
* IsHR
* IsManager
* IsEmployee
* IsOwner
* IsHRorAdmin
* IsDocumentOwnerOrHR

---

# API Security

Implemented security features:

## Throttling

API limits:

* Login API
* Employee API
* Report API

## IP Restriction

Implemented blocked IP management:

* Block unauthorized IP access
* Log security attempts

---

# Middleware Implementation

Custom middleware:

## Request Logging Middleware

Tracks:

* Request URL
* Method
* User
* IP Address
* Query Count
* Response Time

## Response Time Middleware

Tracks slow responses.

## IP Restriction Middleware

Blocks restricted IP addresses.

## Performance Middleware

Tracks:

* Query execution
* Response performance
* Slow requests

---

# Django Signals & Automation

Implemented signals for automation.

## Employee Signals

Automatically performs:

* Employee profile creation
* Audit log creation
* Employee update tracking
* Employee deletion tracking

## Authentication Signals

Tracks:

* User login
* User logout

---

# Service Layer

Business logic is separated into services.

## employee_service.py

Handles:

* Employee pagination
* Employee search

## dashboard_service.py

Provides:

* Total employees
* Active employees
* Inactive employees
* Departments count
* Average salary

## report_service.py

Handles:

* Employee summary
* Department summary

---

# Database Models

## Department

Stores:

* Department name
* Description
* Created date

## Employee

Stores:

* Employee information
* Salary details
* Department
* Joining date
* Documents
* Profile images

## EmployeeProfile

Stores:

* Address
* Emergency contact
* Blood group
* Skills
* Bio

## EmployeeDocument

Stores:

* Document name
* Document type
* File
* Upload date

## BlockedIP

Stores:

* IP Address
* Blocking reason
* Created date

---

# Logging System

Implemented logging:

```
logs/

application.log
error.log
security.log
performance.log
request.log
```

Tracks:

* Application activities
* Errors
* Security events
* API performance
* User requests

---

# Performance Optimization

Implemented:

* Django caching
* Database indexing
* Query optimization
* Select related queries
* Pagination
* Performance monitoring

Caching implemented for:

* Dashboard statistics
* Employee list
* Department list

---

# API Endpoints

## Authentication APIs

```
POST /api/v1/auth/login/

POST /api/v1/auth/refresh/

POST /api/v1/auth/logout/

POST /api/v1/auth/change-password/

POST /api/v1/auth/forgot-password/

POST /api/v1/auth/reset-password/

GET /api/v1/auth/profile/
```

## Employee APIs

```
GET /employees/

GET /employees/search/

POST /employees/import/

GET /employees/export/

POST /employees/csv/import/

GET /employees/csv/export/

GET /employees/<id>/profile-pdf/
```

## Document APIs

```
POST /documents/upload/

GET /documents/

GET /documents/<id>/download/

POST /documents/<id>/delete/
```

---

# How To Run Project

## Clone Repository

```
git clone https://github.com/srinadhatla/Git_work.git
```

## Create Virtual Environment

```
python -m venv venv
```

## Activate Environment

```
venv\Scripts\activate
```

## Install Dependencies

```
pip install -r requirements.txt
```

## Run Migrations

```
python manage.py migrate
```

## Start Server

```
python manage.py runserver
```

---

# Git Information

Repository:

```
https://github.com/srinadhatla/Git_work/tree/feature/file-management-reporting
```

Branch:

```
feature/file-management-reporting
```

---

# Future Enhancements

* Email notification system
* Cloud file storage integration
* Advanced analytics dashboard
* Background task processing
* Production deployment

---

# Author

**Atla Srinadh**

Python Developer
