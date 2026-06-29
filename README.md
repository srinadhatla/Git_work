Employee CRUD Project (Django + PostgreSQL)
Overview

This is a Django project that performs basic Employee CRUD operations:
Create, Read, Update, and Delete employee records using PostgreSQL database.

Features
Add new employees
View employee list
Update employee details
Delete employee records
PostgreSQL database integration
Tech Stack
Python
Django
PostgreSQL
HTML (if used in templates)
Git & GitHub
Project Structure
Git_work/
│
├── employees/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── settings.py
├── urls.py
├── manage.py
Installation Steps
1. Clone repository
git clone https://github.com/srinadhatla/Git_work.git
cd Git_work
2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3. Install dependencies
pip install -r requirements.txt
4. Configure PostgreSQL in settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
5. Run migrations
python manage.py makemigrations
python manage.py migrate
6. Run server
python manage.py runserver
Usage

Open in browser:

http://127.0.0.1:8000/
Branch Info
development → main working branch
feature/employee-crud → feature branch for CRUD operations
Author

Srinadh Reddy Atla
