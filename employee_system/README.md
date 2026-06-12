# Employee Management System

## Overview

This project is a Python-based Employee Management System developed using Object-Oriented Programming (OOP) concepts.

The application allows users to:

* Add employee records
* View employee details
* Search employees
* Update employee information
* Delete employee records
* Store employee data in JSON format
* Calculate employee bonuses
* Validate employee data

---

## Project Structure

```text
employee_system/
│
├── main.py
│
├── models/
│   └── employee.py
│
├── services/
│   └── employee_manager.py
│
├── utils/
│   ├── validator.py
│   └── helper.py
│
├── data/
│   └── employees.json
│
└── README.md
```

---

## Requirements

* Python 3.10 or above

Check Python version:

```bash
python --version
```

---

## How to Run

### Step 1: Open Terminal

Navigate to the project folder:

```bash
cd employee_system
```

### Step 2: Run the Application

```bash
python main.py
```

or

```bash
py main.py
```

---

## Sample Employee Creation

```python
emp_obj = employeeBaseModel(
    emp_id=103,
    emp_name='srinadhreddy',
    emp_email='srinadh@blackroth.in',
    department='backend_dev',
    salary=70000,
    experience=5
)
```

---

## Features

### Add Employee

```python
emp1.add_employee(emp_obj)
```

### View Employees

```python
emp1.view_employees()
```

### Search Employee

```python
emp1.search_employee(102)
```

### Update Employee

```python
emp1.update_employee(
    102,
    {'emp_name': 'Atla'}
)
```

### Delete Employee

```python
emp1.delete_employee(102)
```

### Calculate Bonus

```python
emp1.update_bonus()
```

### Validate Employee Data

```python
emp1.validate_employee_data()
```

---

## Technologies Used

* Python
* Object-Oriented Programming (OOP)
* JSON File Handling
* Exception Handling
* Modular Package Structure

---

## Author

Srinadh Reddy Atla
