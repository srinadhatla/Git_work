# Day 24 – Enterprise HRMS Backend | Leave Management Module

## Overview

Implemented a **production-ready Leave Management Module** for the Enterprise HRMS Backend using **Python, Django, Django REST Framework, and PostgreSQL**.

The module provides a complete leave management workflow, including leave application, approval process, leave balance management, business validations, reporting, analytics, notifications, audit logging, and secure REST APIs.

---

# Technologies Used

- Python
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication
- Django ORM
- OpenPyXL
- ReportLab
- CSV Export
- Coverage.py
- Postman

---

# Features Implemented

## 1. Database Models

### LeaveType

- Leave Name
- Leave Code
- Annual Quota
- Paid/Unpaid Leave
- Description
- Created At
- Updated At

Example:

- Casual Leave (CL)
- Sick Leave (SL)
- Earned Leave (EL)
- Work From Home (WFH)
- Maternity Leave
- Paternity Leave
- Compensatory Off

---

### LeaveBalance

Maintains yearly leave balance for every employee.

Fields:

- Employee
- Leave Type
- Allocated Days
- Used Days
- Remaining Days
- Year

---

### LeaveRequest

Stores employee leave applications.

Fields:

- Employee
- Leave Type
- Start Date
- End Date
- Total Days
- Reason
- Status
- Manager Comments
- HR Comments
- Applied At
- Approved At
- Created At
- Updated At

---

# Leave Workflow

```text
Employee
     │
Apply Leave
     │
Manager Review
     │
HR Review
     │
Approved / Rejected
     │
Leave Balance Updated
```

---

# REST APIs

## Employee APIs

### Apply Leave

```
POST /api/v1/leaves/apply/
```

### View My Leaves

```
GET /api/v1/leaves/my-leaves/
```

### View Leave Balance

```
GET /api/v1/leaves/my-balance/
```

### Cancel Leave

```
PUT /api/v1/leaves/{id}/cancel/
```

---

## Manager APIs

### Pending Leave Requests

```
GET /api/v1/leaves/pending/
```

### Approve Leave

```
PUT /api/v1/leaves/{id}/approve/
```

### Reject Leave

```
PUT /api/v1/leaves/{id}/reject/
```

---

## HR/Admin APIs

### View All Leaves

```
GET /api/v1/leaves/
```

### Leave Report

```
GET /api/v1/leaves/report/
```

### Final Approval

```
PUT /api/v1/leaves/{id}/final-approve/
```

### Company Analytics

```
GET /api/v1/leaves/analytics/?year=2026
```

---

# Business Validations

Implemented the following validations:

- Prevent leave start date in the past
- HR/Admin override for past leave
- End date must be greater than or equal to start date
- Prevent overlapping leave requests
- Validate leave balance availability
- Prevent leave exceeding allocated balance
- Weekend exclusion from leave calculation
- Prevent zero working-day leave requests
- Restore leave balance after cancellation
- Prevent modification of approved leave

---

# Service Layer

Implemented all business logic inside a dedicated service layer.

Functions:

- apply_leave()
- approve_leave()
- reject_leave()
- cancel_leave()
- calculate_leave_days()
- calculate_working_days()
- update_leave_balance()
- employee_leave_summary()
- company_leave_analytics()

Views only call service methods.

---

# Search & Filters

Implemented filtering by:

- Employee
- Department
- Leave Type
- Status
- Date Range
- Year
- Manager

Example:

```
GET /api/v1/leaves/?status=Approved
```

```
GET /api/v1/leaves/?employee=EMP001
```

```
GET /api/v1/leaves/?leave_type=SL
```

```
GET /api/v1/leaves/?year=2026
```

---

# Leave Calendar

Implemented:

- Monthly Leave Calendar
- Team Leave Calendar
- Upcoming Leaves
- Employees Currently on Leave

Dashboard Summary:

- Employees on Leave Today
- Upcoming Leave Requests
- Pending Approvals

---

# Reports & Analytics

Implemented:

## Employee Leave Summary

- Allocated Leave
- Used Leave
- Remaining Leave

## Department Leave Report

- Department-wise Leave Requests
- Leave Utilization

## Company Analytics

- Monthly Leave Trends
- Most Used Leave Type
- Employees with Zero Leave Balance

---

# Export Reports

Implemented:

## PDF

- Employee Leave History

## Excel

- Annual Leave Register

## CSV

- Leave Transactions

---

# Notifications

Implemented notifications for:

- Leave Applied
- Manager Approved
- HR Approved
- Leave Rejected
- Leave Cancelled

---

# Audit Logging

Audit logs generated for:

- Leave Applied
- Manager Approved
- HR Approved
- Leave Rejected
- Leave Cancelled

---

# Testing

Created automated tests for:

- Models
- Services
- APIs
- Permissions

Current Result:

```
Found 5 test(s).

.....
----------------------------------------------------------------------
Ran 5 tests

OK
```

---

# How to Run the Project

Activate virtual environment

```bash
venv\Scripts\activate
```

Run migrations

```bash
python manage.py migrate
```

Run server

```bash
python manage.py runserver
```

---

# How to Test APIs

## 1. Login

```
POST /api/v1/auth/login/
```

Copy the Access Token.

Add the token in Postman.

```
Authorization

Bearer <access_token>
```

---

## 2. Apply Leave

```
POST /api/v1/leaves/apply/
```

Example JSON

```json
{
    "leave_type": 1,
    "start_date": "2026-08-20",
    "end_date": "2026-08-22",
    "reason": "Family Function"
}
```

Expected Result

- Leave request created
- Status = Pending

---

## 3. View My Leaves

```
GET /api/v1/leaves/my-leaves/
```

Expected Result

Returns logged-in employee leave history.

---

## 4. View Leave Balance

```
GET /api/v1/leaves/my-balance/
```

Expected Result

Returns

- Allocated
- Used
- Remaining

---

## 5. Manager Approval

```
PUT /api/v1/leaves/{id}/approve/
```

Expected Result

Status changes to

```
MANAGER_APPROVED
```

---

## 6. Reject Leave

```
PUT /api/v1/leaves/{id}/reject/
```

Expected Result

```
REJECTED
```

---

## 7. HR Final Approval

```
PUT /api/v1/leaves/{id}/final-approve/
```

Expected Result

```
APPROVED
```

Leave balance updated automatically.

---

## 8. Cancel Leave

```
PUT /api/v1/leaves/{id}/cancel/
```

Expected Result

- Status = Cancelled
- Leave balance restored

---

## 9. Analytics

```
GET /api/v1/leaves/analytics/?year=2026
```

Expected Result

Returns

- Monthly Trends
- Department Report
- Most Used Leave Type
- Zero Leave Balance Employees

---

## 10. Export PDF

```
GET /api/v1/leaves/reports/pdf/
```

Downloads

```
leave_history.pdf
```

---

## 11. Export Excel

```
GET /api/v1/leaves/reports/excel/
```

Downloads

```
leave_register.xlsx
```

---

## 12. Export CSV

```
GET /api/v1/leaves/reports/csv/
```

Downloads

```
leave_transactions.csv
```

---

# Run Unit Tests

```bash
python manage.py test leave_management.tests
```

Expected Output

```
Found 5 test(s).

.....

----------------------------------------------------------------------
Ran 5 tests

OK
```

---

# Generate Coverage Report

Run

```bash
coverage run manage.py test leave_management.tests
```

Generate Report

```bash
coverage report
```

Generate HTML Report

```bash
coverage html
```

Open

```
htmlcov/index.html
```

---

# Project Structure

```
leave_management/
│
├── migrations/
├── services/
│   └── leave_service.py
├── tests/
│   ├── test_models.py
│   ├── test_services.py
│   ├── test_api.py
│   └── test_permissions.py
├── admin.py
├── filters.py
├── models.py
├── notifications.py
├── permissions.py
├── reports.py
├── serializers.py
├── urls.py
├── utils.py
├── validators.py
└── views.py
```

---

# Learning Outcomes

During this implementation, I gained hands-on experience with:

- Enterprise HRMS backend architecture
- Django Service Layer pattern
- Multi-level approval workflow
- Leave balance management
- Business rule implementation
- Weekend-aware leave calculation
- HR/Admin override validation
- Django ORM optimization
- Report generation using ReportLab and OpenPyXL
- CSV export
- Notifications
- Audit logging
- REST API development using Django REST Framework
- Unit testing
- Code coverage analysis

---

# Git Commands

```bash
git checkout development

git pull origin development

git checkout -b feature/leave-management

git add .

git commit -m "Implemented production-ready Leave Management module"

git push origin feature/leave-management
```

---

# Module Status

**Sprint:** HRMS Backend Sprint 2

**Module:** Leave Management

**Priority:** Critical

**Status:** ✅ Completed Successfully