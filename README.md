# 🔐 Employee User Management System (Django HRMS)

A Django-based **Authentication and Role-Based Access Control (RBAC)** system for managing employees, departments, and users with different roles like Admin, HR, Manager, and Employee.

---

## 🚀 Project Overview

This project demonstrates a complete authentication system including:

- User Registration
- Login & Logout
- Custom User Model
- Role-Based Access Control (RBAC)
- Permission & Group Management
- Dashboard Redirection
- Profile Management
- Password Reset System

---

## 🏗️ Project Structure
company_portal/
│
├── accounts/
│ ├── models.py
│ ├── forms.py
│ ├── views.py
│ ├── urls.py
│ ├── decorators.py
│ ├── permissions.py
│ ├── admin.py
│ └── templates/accounts/
│ ├── register.html
│ ├── login.html
│ ├── profile.html
│ └── dashboard.html
│
├── employees/
├── departments/
├── media/
├── requirements.txt
└── manage.py


---

## 🔐 Features

### 👤 Authentication
- Secure login/logout system
- Session management
- Password hashing

### 🧑 Custom User Model
- Email-based login
- Employee ID (EMP001 format)
- Phone number
- Profile image
- Role field (ADMIN, HR, MANAGER, EMPLOYEE)

### 📝 Registration
- Strong password validation
- Unique email & employee ID
- Role selection

### 🔑 Login & Logout
- Session-based authentication
- Redirect to role-based dashboard

### 🛡️ RBAC (Role-Based Access Control)
- Admin → Full access
- HR → Employee management
- Manager → Department access
- Employee → Own profile only

### 👥 Django Groups & Permissions
- Admin
- HR
- Manager
- Employee
- CRUD permissions for Employee model

### 📊 Dashboards
- Admin Dashboard → statistics overview
- HR Dashboard → employee management
- Employee Dashboard → personal details

### 🔒 Password Management
- Change password
- Forgot password
- Reset password via email token

### 👤 Profile Management
- Update profile image
- Edit personal details
- Change password

---

## 🔁 Authentication Flow

User Login
↓
Authentication Check
↓
Session Created
↓
Role Verified
↓
Dashboard Redirect



## ⚙️ Installation

```bash
git clone https://github.com/srinadhatla/Git_work.git

cd Git_work

python -m venv venv

venv\Scripts\activate   # Windows

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
