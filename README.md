# HRMS Automation System - Django Project

## Project Overview

**HRMS Automation System** is an enterprise-level Human Resource Management System built using Django.

This project demonstrates real-world backend development concepts including:

* Django Models
* Django Signals
* Custom Middleware
* Audit Logging
* Performance Monitoring
* Custom Management Commands
* Django Admin Customization
* Database Optimization
* Query Optimization
* Caching
* Employee Management Automation

The application manages employee records, departments, employee profiles, audit activities, security monitoring, reports generation, and automated HR operations.

---

# Technology Stack

## Backend

* Python
* Django 6.0.6

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
* Django Admin

---

# Project Features

## 1. Employee Management Module

Implemented employee management functionality.

Features:

* Create employees
* Update employee details
* Delete employees
* Employee profile creation
* Department assignment
* Salary tracking
* Employee status management

Employee fields:

* Employee ID
* First Name
* Last Name
* Email
* Phone
* Department
* Designation
* Salary
* Joining Date
* Active Status

---

# 2. Department Management

The system manages company departments.

Implemented:

* Department creation
* Department listing
* Employee count by department
* Department audit tracking

Example departments:

```
HR
IT
Finance
Marketing
Operations
Testing
Security
Admin
Support
```

---

# 3. Employee Profile Management

Automatically creates employee profiles using Django Signals.

Profile contains:

* Address
* Emergency Contact
* Blood Group
* Profile Photo
* Skills
* Biography

---

# 4. Django Signals Implementation

Implemented automatic background operations using Django Signals.

## Employee Created Signal

When a new employee is created:

Actions performed:

* Creates Employee Profile automatically
* Creates Audit Log entry
* Writes application logs

Example:

```
Welcome Employee Name! Employee Profile Created.
```

## Employee Updated Signal

Tracks:

* Salary changes
* Department changes

Stores previous values:

```
previous_salary
previous_department
```

## Employee Deleted Signal

Creates audit history when employees are deleted.

## User Authentication Signals

Tracks:

* User Login
* User Logout

Stored information:

* Username
* IP Address
* Request Method
* Timestamp

---

# 5. Custom Middleware Implementation

## IP Restriction Middleware

Blocks unwanted IP addresses.

Features:

* Checks incoming request IP
* Compares with blocked IP database
* Prevents unauthorized access

Example response:

```
403 Forbidden - Your IP is blocked.
```

---

## Request Logging Middleware

Tracks every request:

Captured details:

```
URL
HTTP Method
User
IP Address
Query Count
Response Time
```

Example:

```
URL : /employees/
Method : GET
User : admin
IP : 127.0.0.1
Queries : 5
Response Time : 20 ms
```

---

## Response Time Middleware

Monitors slow requests.

If response time exceeds 500ms:

Logs warning.

Example:

```
Slow Response: /dashboard/ took 700 ms
```

---

## Performance Middleware

Tracks application performance:

Includes:

* Database query count
* Execution time
* User details

---

# 6. Audit Logging System

Implemented a separate audit logging application.

Application:

```
audit_logs
```

Tracks:

* Employee Created
* Employee Updated
* Employee Deleted
* Department Created
* User Login
* User Logout

Stored information:

```
User
Action
Module
Object ID
IP Address
Request Method
Timestamp
```

---

# 7. Custom Management Commands

Created Django automation commands.

## Generate Sample Data

Command:

```bash
python manage.py seed_data
```

Output:

```
Departments created.

5000 Employees created successfully.
```

Creates:

* 9 Departments
* 5000 Employees

---

## Generate HR Reports

Command:

```bash
python manage.py generate_reports
```

Output:

```
Reports Generated Successfully
```

Generated files:

```
reports/

employees_summary.txt

department_summary.txt

salary_summary.txt
```

---

## Deactivate Inactive Employees

Command:

```bash
python manage.py deactivate_inactive_users
```

Function:

* Finds employees older than 180 days
* Changes active status to False
* Generates inactive employee report

Output:

```
Employees deactivated successfully.
```

Generated report:

```
reports/inactive_users_report.txt
```

---

# 8. Dashboard Module

Dashboard displays HR statistics.

Displayed information:

* Total Employees
* Active Employees
* Inactive Employees
* Total Departments
* Employees Joined Today
* Average Salary
* Department Employee Count

URL:

```
http://127.0.0.1:8000/dashboard/
```

---

# 9. Employee Search

Implemented employee searching functionality.

Search supported:

* Employee ID
* First Name
* Last Name
* Email
* Department
* Active Status

URL:

```
http://127.0.0.1:8000/employees/search/
```

---

# 10. Performance Optimization

Implemented:

## Database Optimization

Used:

```
select_related()
prefetch_related()
only()
```

## Database Indexing

Added indexes for:

```
Employee Status
Joining Date
Department
Employee ID
Email
```

## Caching

Implemented Django cache.

Cached:

* Dashboard statistics
* Employee list
* Department list

Cache backend:

```
LocMemCache
```

---

# 11. Django Admin Customization

Admin features:

Employee Admin:

* Search employees
* Filter employees
* Date hierarchy
* Bulk activate employees
* Bulk deactivate employees
* Export employees CSV

Department Admin:

* Department listing
* Search

Employee Profile Admin:

* Profile management

Blocked IP Admin:

* Security management

---

# Project Structure

```
company_portal15

│
├── manage.py
├── db.sqlite3
├── requirements.txt
│
├── company_portal
│   ├── settings.py
│   ├── urls.py
│   ├── middleware.py
│   └── views.py
│
├── employees
│   ├── models.py
│   ├── views.py
│   ├── signals.py
│   ├── admin.py
│   │
│   ├── management
│   │   └── commands
│   │       ├── seed_data.py
│   │       ├── generate_reports.py
│   │       └── deactivate_inactive_users.py
│   │
│   └── services
│       ├── dashboard_service.py
│       ├── employee_service.py
│       └── report_service.py
│
├── audit_logs
│
├── logs
│   ├── application.log
│   ├── request.log
│   ├── security.log
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

## Install Dependencies

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

Application runs at:

```
http://127.0.0.1:8000/
```

---

# Output Screenshots

Add screenshots here:

## Dashboard

```
docs/dashboard.png
```

## Employee List

```
docs/employees_list.png
```

## Django Admin

```
docs/admin.png
```

## Management Commands

```
docs/commands.png
```

## Logs

```
docs/logs.png
```

---

# Reports Generated

Example:

```
reports/

employees_summary.txt

department_summary.txt

salary_summary.txt

inactive_users_report.txt

```

---

# Learning Outcomes

Through this project implemented:

* Django MVC architecture
* ORM optimization
* Signals automation
* Middleware development
* Logging architecture
* Database indexing
* Caching strategy
* Admin customization
* Backend automation
* Enterprise HRMS workflow

---

# Future Enhancements

Possible improvements:

* REST API development using Django REST Framework
* JWT Authentication
* Role Based Access Control
* PostgreSQL Database
* Docker Deployment
* Cloud Deployment
* Employee Attendance Module
* Payroll Automation

---

# Author

**Srinadh Reddy Atla**

Python Backend Developer

Skills:

Python | Django | SQL | REST API | Git | PostgreSQL
