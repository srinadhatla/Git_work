Company Portal – Django HR Management System (PostgreSQL)
Overview :

This project is a Django-based HR Management System built using PostgreSQL. It demonstrates core database concepts, Django ORM, and full CRUD operations for managing employees and departments.

The project is designed as a learning + practical implementation of real-world HR systems.

Features :
Employee Management System
Department Management System
PostgreSQL Database Integration
Django ORM CRUD Operations
Django Admin Panel Customization
Search & Filtering functionality
Relationship handling (Foreign Key between Employee & Department)
🛠️ Tech Stack
Python
Django 
PostgreSQL
Django ORM
HTML (Django Templates)
Git & GitHub
Database Concepts Used :
Tables
employees
departments
Key Concepts
Primary Key → employee_id
Foreign Key → Employee → Department
One-to-Many Relationship
Relational Database Design

Project Structure :
company_portal/
│
├── manage.py
│
├── employees/
│   ├── models.py
│   ├── admin.py
│   ├── views.py
│   ├── urls.py
│   ├── migrations/
│
├── departments/
│   ├── models.py
│   ├── admin.py
│   ├── migrations/
│
├── company_portal/
│   ├── settings.py
│   ├── urls.py
│
├── requirements.txt
└── README.md
PostgreSQL Setup :
Create Database
CREATE DATABASE employee_management;
Create User
CREATE USER employee_admin WITH PASSWORD 'password123';
GRANT ALL PRIVILEGES ON DATABASE employee_management TO employee_admin;
⚙️ Django Database Configuration

In settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'employee_management',
        'USER': 'employee_admin',
        'PASSWORD': 'password123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Models :
Department Model
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
Employee Model
class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField()
    designation = models.CharField(max_length=100)
    status = models.CharField(max_length=20)

    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
Setup Instructions
1. Clone Repository
git clone https://github.com/srinadhatla/Git_work.git
cd Git_work
git checkout feature/models-postgresql
2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3. Install Dependencies
pip install -r requirements.txt
4. Run Migrations
python manage.py makemigrations
python manage.py migrate
5. Create Superuser
python manage.py createsuperuser
6. Run Server
python manage.py runserver
🧪 Django ORM Operations
Create Employee
Employee.objects.create(
    employee_id="EMP001",
    first_name="Ajay",
    email="ajay@example.com",
    salary=50000
)
Retrieve Data
Employee.objects.all()
Filter Data
Employee.objects.filter(department__name="Engineering")
Update Data
employee.salary = 70000
employee.save()
Delete Data
employee.delete()
🧾 Admin Panel Features
Employee Management
Department Management
Search functionality
Filters by Department
Custom list display fields
📚 Learning Outcomes
Database design using relational models
PostgreSQL integration with Django
Django ORM CRUD operations
Admin panel customization
Real-world HR system structure
Git feature branch workflow
👨‍💻 Author

Srinadh Reddy Atla

📌 Git Workflow Used
git checkout development
git pull origin development
git checkout -b feature/models-postgresql
