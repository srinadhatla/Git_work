# Django Signals, Middleware & Custom Management Commands — HRMS Automation Module

## Project Overview
Day - 14:

This project implements enterprise-level HRMS automation features using Django built-in capabilities such as:

* Django Signals
* Custom Middleware
* Custom Management Commands
* Logging System
* Audit Trail
* Exception Handling
* Admin Customization
* Data Validation
* Dashboard Analytics

The goal of this module is to automate employee management operations similar to real-world HRMS, ERP, CRM, Banking, and E-commerce backend systems.

---

# Company Scenario

The HRMS application requires the following automation:

✅ Automatically create Employee Profile when a new Employee is added
✅ Track employee CRUD operations
✅ Maintain audit history
✅ Log user login and logout activity
✅ Track request processing time
✅ Block restricted IP addresses
✅ Generate employee reports automatically
✅ Manage inactive users
✅ Provide enterprise-level logging and error handling

---

# Features Implemented

## 1. Django Signals

### Implemented Signals

* `post_save`
* `pre_save`
* `post_delete`
* `m2m_changed`

### Employee Automation

When a new employee is created:

```
Employee Created
        |
        ↓
post_save Signal
        |
        ↓
Create Employee Profile
        |
        ↓
Create Audit Log
        |
        ↓
Send Notification
```

### Signal Tasks

Implemented:

* Automatically create EmployeeProfile
* Create employee audit record
* Store joining date
* Track previous salary changes
* Track previous department changes
* Archive deleted employee data
* Create delete logs

---

# 2. Employee Profile Automation

## Employee Model

Employee information includes:

* Employee ID
* Name
* Department
* Salary
* Joining Date
* Contact Details

## EmployeeProfile Model

Automatically created after employee registration.

Fields:

* Employee
* Address
* Emergency Contact
* Blood Group
* Profile Photo
* Skills
* Bio

---

# 3. Audit Logging System

## AuditLog Model

Stores complete activity history.

Fields:

```
id
user
action
module
object_id
timestamp
ip_address
request_method
```

## Logged Activities

The system records:

* Employee Created
* Employee Updated
* Employee Deleted
* Department Created
* User Login
* User Logout

---

# 4. Django Middleware

Custom middleware handles request processing.

## Request Logging Middleware

Tracks:

* URL
* HTTP Method
* User
* IP Address
* Response Status
* Processing Time

Logs stored in:

```
logs/request.log
```

## Response Time Middleware

Calculates:

```
Start Time
      |
      ↓
Process Request
      |
      ↓
End Time
      |
      ↓
Total Response Time
```

If response time is greater than 500ms:

```
WARNING: Slow Response
```

## IP Restriction Middleware

Blocked users are managed using:

## BlockedIP Model

Fields:

```
ip_address
reason
created_at
```

Blocked requests return:

```
403 Forbidden
```

---

# 5. Custom Management Commands

Created custom Django commands.

Location:

```
employees/
    management/
        commands/
```

## Generate Reports

Command:

```bash
python manage.py generate_reports
```

Generates:

* Employee Summary
* Department Summary
* Salary Summary

Reports saved inside:

```
reports/
```

## Deactivate Inactive Users

Command:

```bash
python manage.py deactivate_inactive_users
```

Functionality:

* Finds users inactive for more than 180 days
* Marks users inactive
* Generates inactive user report

## Seed Data Command

Command:

```bash
python manage.py seed_data
```

Creates:

* 10 Departments
* 100 Employees
* 20 Managers

---

# 6. Django Logging System

Logging configuration implemented.

Log files:

```
logs/
│
├── application.log
├── error.log
└── security.log
```

## Logged Events

### INFO

Example:

```
Employee Created Successfully
```

### WARNING

Example:

```
Slow Response Detected
```

### ERROR

Example:

```
Database Connection Error
```

### SECURITY

Example:

```
Unauthorized Access Attempt
```

---

# 7. Exception Handling

Custom error pages created:

```
templates/

├── 403.html
├── 404.html
└── 500.html
```

Pages display:

* Error Code
* Friendly Message
* Dashboard Navigation Link

---

# 8. Django Admin Enhancements

Customized Django Admin Panel.

Implemented:

* Search Filters
* Date Hierarchy
* Readonly Fields
* Bulk Actions

Admin Actions:

* Export Employees CSV
* Activate Employees
* Deactivate Employees

---

# 9. HRMS Dashboard Analytics

Dashboard displays:

## Employee Statistics

* Total Employees
* Active Employees
* Departments
* Employees Joined Today
* Employees Joined This Month
* Inactive Users

## Salary Analytics

* Salary Distribution
* Department Salary Reports

---

# 10. Data Validation

Implemented model validation.

Rules:

### Salary Validation

Salary cannot be negative.

Example:

```
salary >= 0
```

### Joining Date Validation

Joining date cannot be future date.

### Employee ID Protection

Employee ID cannot be changed after creation.

Implemented using:

* clean()
* save() override
* Custom validators

---

# Project Structure

```
company_portal/

│
├── employees/
│
│   ├── models.py
│   ├── signals.py
│   ├── middleware.py
│   ├── validators.py
│   ├── admin.py
│
│   └── management/
│       └── commands/
│
│           ├── generate_reports.py
│           ├── seed_data.py
│           └── deactivate_inactive_users.py
│
├── audit_logs/
│
├── reports/
│
├── logs/
│
└── templates/
    ├── 403.html
    ├── 404.html
    └── 500.html

```

---

# Installation & Setup

## Clone Repository

```bash
git clone https://github.com/srinadhatla/Git_work.git
```

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Database Migration

```bash
python manage.py makemigrations

python manage.py migrate
```

## Create Super User

```bash
python manage.py createsuperuser
```

## Start Server

```bash
python manage.py runserver
```

---

# Testing Commands

Run report generation:

```bash
python manage.py generate_reports
```

Generate sample data:

```bash
python manage.py seed_data
```

Deactivate inactive users:

```bash
python manage.py deactivate_inactive_users
```

---

# Git Workflow

Feature branch:

```
feature/django-signals-middleware
```

Commands used:

```bash
git checkout development

git pull origin development

git checkout -b feature/django-signals-middleware
```

Commit changes:

```bash
git add README.md

git commit -m "Add README documentation for Django signals middleware module"

git push origin feature/django-signals-middleware
```

---

# Learning Outcomes

After completing this module, the following Django enterprise concepts are covered:

* Django Signal Automation
* Request Lifecycle Management
* Middleware Development
* Audit Trail Implementation
* Background Automation Commands
* Logging Architecture
* Error Handling
* Admin Customization
* Backend Validation

---

# Project Status

🚧 Development In Progress

Module: Day 14 — Django Signals, Middleware & Custom Management Commands

Branch:

```
feature/django-signals-middleware
```
