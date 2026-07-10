# HRMS Secure REST API Platform - Django Project

## Project Overview

**HRMS Secure REST API Platform** is an enterprise-level Human Resource Management System built using Django and Django REST Framework.

This project demonstrates secure backend API development concepts required for modern enterprise applications used by:

* React Admin Portal
* Flutter Mobile Applications
* HR Dashboards
* Third-Party Payroll Systems

The system implements secure authentication, authorization, employee management, security logging, API protection, and HR automation features.

Major backend concepts implemented:

* JWT Authentication
* Access Token and Refresh Token Flow
* Token Blacklisting Logout
* Password Management APIs
* Role-Based Authorization
* Object-Level Permissions
* API Rate Limiting
* Secure File Upload Validation
* Security Audit Logging
* Employee Management
* Django Middleware
* Report Generation

---

# Technology Stack

## Backend

* Python 3.13.2
* Django 6.0.6
* Django REST Framework

## Authentication

* JSON Web Token (JWT)
* djangorestframework-simplejwt
* Refresh Token Rotation
* Token Blacklisting

## Database

* SQLite3

## Frontend

* Django Templates
* HTML
* CSS

## Development Tools

* VS Code
* Git
* GitHub
* Postman
* Django Admin

---

# Project Scenario

The HRMS application provides secure APIs for multiple clients:

* React Admin Portal
* Flutter Mobile App
* HR Dashboard
* External Payroll Systems

The company requires:

* Secure user login
* JWT authentication
* Refresh token support
* Logout with token revocation
* Password recovery
* Role-based API access
* Unauthorized access prevention
* Security monitoring

---

# Authentication Architecture

## JWT Authentication Flow

```
User Login

      |
      ▼

Access Token
+
Refresh Token

      |
      ▼

Protected API Access

      |
      ▼

Access Token Expired

      |
      ▼

Refresh Token

      |
      ▼

New Access Token
```

---

# Authentication APIs

Base URL:

```
http://127.0.0.1:8000/api/v1/auth/
```

---

# 1. Login API

## Endpoint

```
POST /api/v1/auth/login/
```

## Features

* User authentication
* JWT access token generation
* JWT refresh token generation
* Login security logging
* Login throttling protection

## Request

```json
{
    "username":"atlasrinadh",
    "password":"@Comrade3"
}
```

## Response

```json
{
    "username":"admin",
    "access":"jwt_access_token",
    "refresh":"jwt_refresh_token"
}
```

---

# 2. Refresh Token API

## Endpoint

```
POST /api/v1/auth/refresh/
```

## Features

* Generates new access token
* Validates refresh token
* Handles invalid tokens

Request:

```json
{
    "refresh":"refresh_token"
}
```

Response:

```json
{
    "access":"new_access_token"
}
```

---

# 3. Logout API

## Endpoint

```
POST /api/v1/auth/logout/
```

## Features

* Refresh token blacklisting
* Prevents token reuse
* Security event logging

Response:

```json
{
    "message":"Logout successful"
}
```

---

# 4. Change Password API

## Endpoint

```
POST /api/v1/auth/change-password/
```

## Features

* Verify current password
* Validate new password
* Hash password securely
* Log password changes

Request:

```json
{
    "current_password":"@Srinadh3",
    "new_password":"@Comrade3"
}
```

---

# 5. Forgot Password API

## Endpoint

```
POST /api/v1/auth/forgot-password/
```

## Features

* Email validation
* Generates password reset token
* Token expiration support
* Security logging

Token expiry:

```
15 minutes
```

---

# 6. Reset Password API

## Endpoint

```
POST /api/v1/auth/reset-password/
```

## Features

* Reset token validation
* Expired token rejection
* Password update
* Token deletion after reset

---

# 7. User Profile API

## Endpoint

```
GET /api/v1/auth/profile/
```

## Features

* JWT protected API
* User-specific profile access
* Object-level permission checking

Response:

```json
{
    "id":1,
    "username":"atla",
    "email":"atla@blackroth.in"
}
```

---

# Role Based Authorization

Custom permission classes implemented:

```
accounts/permissions.py
```

Implemented:

* IsAdmin
* IsHR
* IsManager
* IsEmployee
* IsOwner

---

# Permission Features

## Admin

Access:

* Employee Management
* Reports
* Administrative APIs

## HR

Access:

* Employee operations
* HR related APIs

## Manager

Access:

* Manager-level resources

## Employee

Access:

* Personal profile information

---

# Object Level Permissions

Implemented:

```
IsOwner
```

Purpose:

Employees can access only their own profile data.

Example:

Allowed:

```
GET /api/v1/auth/profile/
```

Restricted:

```
GET another employee profile
```

---

# API Rate Limiting

Custom throttle classes:

```
LoginRateThrottle

EmployeeRateThrottle

ReportRateThrottle
```

Configured limits:

| API          | Limit               |
| ------------ | ------------------- |
| Login API    | 5 requests/minute   |
| Employee API | 100 requests/minute |
| Report API   | 20 requests/minute  |

---

# Secure File Upload Validation

Employee profile image upload is protected.

Validation rules:

Allowed:

```
.jpg
.jpeg
.png
```

Maximum size:

```
2 MB
```

Validation includes:

* Extension validation
* File size validation
* MIME type validation

Rejected:

```
.exe
.zip
.js
.bat
```

---

# Employee Management Module

Implemented employee management functionality.

Features:

* Employee listing
* Department management
* Employee searching
* Profile management
* Salary tracking
* Status management

---

# Employee Fields

```
Employee ID

First Name

Last Name

Email

Phone

Department

Designation

Salary

Joining Date

Active Status

Profile Image
```

---

# Employee Validation

Implemented validations:

## Employee ID

Format:

```
EMP00001
```

## Email

* Valid email format
* Unique email validation

## Phone

Rules:

```
10 digit number
```

## Salary

Rules:

```
Salary must be positive
```

## Joining Date

Rule:

```
Cannot be future date
```

---

# Security Logging System

Application:

```
logs
```

Security events stored in:

```
SecurityLog
```

Tracked events:

* Login Success
* Login Failed
* Password Change
* Password Reset
* Unauthorized Access
* Permission Denied
* Token Blacklisted

---

# SecurityLog Model

Fields:

```
User

IP Address

Action

Status

Timestamp
```

---

# Middleware Implementation

Implemented custom middleware:

## IP Restriction Middleware

Features:

* Blocks restricted IP addresses
* Prevents unauthorized requests

## Request Logging Middleware

Tracks:

```
URL

HTTP Method

User

IP Address

Response Time
```

## Performance Middleware

Tracks:

```
Database queries

Execution time

Application performance
```

---

# Reports Generated

Generated reports:

```
reports/

employees_summary.txt

department_summary.txt

salary_summary.txt

inactive_users_report.txt
```

---

# Project Structure

```
company_portal18

│
├── manage.py
├── db.sqlite3
├── requirements.txt
│
├── accounts
│   ├── authentication.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── security.py
│   ├── throttles.py
│   ├── validators.py
│   ├── views.py
│   └── urls.py
│
├── employees
│   ├── models.py
│   ├── serializers.py
│   ├── signals.py
│   ├── validators.py
│   │
│   ├── services
│   │   ├── dashboard_service.py
│   │   ├── employee_service.py
│   │   └── report_service.py
│   │
│   └── management
│       └── commands
│           ├── seed_data.py
│           ├── generate_reports.py
│           └── deactivate_inactive_users.py
│
├── audit_logs
│
├── logs
│   ├── security.log
│   ├── request.log
│   ├── application.log
│   ├── error.log
│   └── performance.log
│
├── reports
│
└── templates
```

---

# Installation and Setup

## Clone Repository

```bash
git clone <repository-url>
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

## Apply Migrations

```bash
python manage.py migrate
```

---

## Create Super User

```bash
python manage.py createsuperuser
```

---

## Run Server

```bash
python manage.py runserver
```

Application:

```
http://127.0.0.1:8000/
```

---

# API Testing

Testing tool:

```
Postman
```

Tested APIs:

```
Login API

Refresh Token API

Logout API

Change Password API

Forgot Password API

Reset Password API

Profile API
```

---

# Output Screenshots

Add screenshots:

```
docs/

login.png

refresh_token.png

logout.png

change_password.png

forgot_password.png

profile.png

employee_list.png

dashboard.png

security_logs.png

admin.png
```

---

# Learning Outcomes

Through this project implemented:

* Secure JWT Authentication
* REST API Development
* Token Management
* Role Based Access Control
* Object Level Permissions
* API Security
* Password Management
* File Upload Security
* Database Logging
* Middleware Development
* Django Backend Architecture

---

# Future Enhancements

Possible improvements:

* PostgreSQL Production Deployment
* Docker Containerization
* Cloud Deployment
* React Admin Dashboard
* Flutter Mobile Integration
* Advanced RBAC
* API Documentation using Swagger
* Employee Attendance System
* Payroll Automation

---

# Author

**Srinadh Reddy Atla**

Python Backend Developer

Skills:

Python | Django | Django REST Framework | SQL | REST API | Git | PostgreSQL
