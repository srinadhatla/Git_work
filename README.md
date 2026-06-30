Django Training Project – Company Employee Portal

This project is part of Django training where we build a Company Employee Portal using Django framework step by step.

---

What is Django

Django is a high-level Python web framework used to build secure, scalable, and maintainable web applications.

Companies use Django because it provides:

- Rapid development
- Built-in Admin Panel
- ORM (Object Relational Mapping)
- Security features
- Authentication system
- Scalable architecture
- Large ecosystem


Django MVT Architecture

Django follows MVT (Model – View – Template) pattern.

Model
- Defines database structure
- Handles database operations
- Represents business data

Example:
Employee:
- id
- name
- email
- salary

View
- Handles incoming requests
- Contains business logic
- Returns response

Flow:
Request → View → Response


Template
- Handles UI (HTML pages)
- Displays data to users

Flow:
View → Template → HTML Page

Full MVT Flow
Browser Request  
→ URL  
→ View  
→ Model (Database)  
→ Template  
→ Response  


Django Environment Setup

Create virtual environment:
python -m venv venv
Activate virtual environment:

venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac

Install Django:

pip install django

Check Django version:

python -m django --version

Save dependencies:

pip freeze > requirements.txt
Create Django Project
django-admin startproject company_portal
cd company_portal
python manage.py runserver

Project structure:

company_portal/
├── manage.py
└── company_portal/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
Create Django App
python manage.py startapp employees

Add app in settings.py:

INSTALLED_APPS = [
    "employees",
]
Django URLs and Views
Simple View
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Company Employee Portal")
App URLs
from django.urls import path
from .views import home

urlpatterns = [
    path("", home),
]
Project URLs
from django.urls import path, include

urlpatterns = [
    path("", include("employees.urls")),
]
Django Templates

Create:

employees/templates/employees/home.html

Example HTML:

<h1>Employee Management Portal</h1>
<p>Welcome to Django Training</p>

Render in view:

from django.shortcuts import render

def home(request):
    return render(request, "employees/home.html")
Static Files (CSS)

Structure:

employees/static/employees/css/style.css

Example CSS:

h1 {
    color: blue;
}
Practical Tasks
Task 1: Pages to Create
Home Page
About Page
Contact Page

Each page should include:

Company information
Technology stack
Team details
Contact details
Task 2: Multi Page Navigation

Routes:

/ 
/about/
/contact/

Requirements:

Separate views for each page
Templates for each page
Navigation menu
CSS styling
Final Project Structure
company_portal/
├── manage.py
├── requirements.txt
├── README.md
│
├── company_portal/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── employees/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── employees/
│   │       ├── home.html
│   │       ├── about.html
│   │       └── contact.html
│   │
│   └── static/
│       └── employees/
│           └── css/
│               └── style.css
│
└── .gitignore
Git Workflow
git checkout development
git pull origin development
git checkout -b feature/django-project-setup
Author

Srinadh Reddy Atla
