# Attendance Management API Documentation

Base URL:

http://127.0.0.1:8000/api/v1/attendance/


## Authentication

All APIs require JWT Authentication.

Header:

Authorization: Bearer <access_token>


---

# Employee APIs


## 1. Employee Check-In

Endpoint:

POST /check-in/


Request:

{
    "remarks": "Started office work"
}


Response:

{
    "attendance_date": "2026-07-30",
    "check_in_time": "2026-07-30T09:00:00Z",
    "attendance_status": "Present"
}



---

## 2. Employee Check-Out

Endpoint:

POST /check-out/


Request:

{
    "break_hours": 1,
    "remarks": "Completed work"
}


Response:

{
    "check_out_time": "2026-07-30T18:00:00Z",
    "working_hours": "8.00",
    "overtime_hours": "0.00"
}



---

## 3. My Attendance History

Endpoint:

GET /my-attendance/


Response:

[
    {
        "date":"2026-07-30",
        "status":"Present",
        "working_hours":"8.00"
    }
]



---

## 4. My Attendance Summary

Endpoint:

GET /my-summary/


Response:

{
    "total_days":25,
    "present_days":23,
    "absent_days":1,
    "leave_days":1,
    "total_working_hours":"184.00"
}



---

# HR/Admin APIs


## Attendance List

GET /

Returns all employees attendance records.



---

## Attendance Detail

GET /{id}/


PUT /{id}/


DELETE /{id}/



---

# Attendance Report


GET /report/?month=7&year=2026


Response:

{
    "total_working_days":22,
    "present_days":20,
    "absent_days":1,
    "leave_days":1,
    "total_working_hours":"160.00"
}



---

# Dashboard API


GET /dashboard/


Response:

{
    "present_count":40,
    "absent_count":5,
    "late_employees":3,
    "employees_not_checked_out":4
}



---

# Analytics APIs


## Department Attendance

GET:

/analytics/departments/


Response:

[
 {
    "department":"Engineering",
    "present":35,
    "absent":5,
    "percentage":87.5
 }
]



## Employee Performance

GET:

/analytics/employees/


Response:

[
 {
    "employee_id":"EMP001",
    "attendance_percentage":95,
    "average_working_hours":8.5,
    "total_overtime":10
 }
]



---

# Export APIs


Excel:

GET /export/excel/


CSV:

GET /export/csv/


PDF:

GET /export/pdf/{employee_id}/