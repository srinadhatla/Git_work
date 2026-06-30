Employee CRUD Project (Django + PostgreSQL)

This project performs basic CRUD operations for employee management using Django and PostgreSQL.

Tech Stack: Python, Django, PostgreSQL

Clone the project:
git clone https://github.com/srinadhatla/Git_work.git
cd Git_work

Create virtual environment:
python -m venv venv
venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Configure PostgreSQL in settings.py:
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

Run migrations:
python manage.py makemigrations
python manage.py migrate

Run server:
python manage.py runserver

Open in browser:
http://127.0.0.1:8000/

Project Structure:
Git_work/
├── employees/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── settings.py
├── urls.py
├── manage.py

Branches:
development - main branch
feature/employee-crud - CRUD feature branch

Author:
Srinadh Reddy Atla
