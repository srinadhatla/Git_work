from services.employee_manager import Employee
from models.employee import employeeBaseModel

if __name__ == "__main__":
    emp_obj = employeeBaseModel(
                                emp_id=103,
                                emp_name= 'srinadhreddy',
                                emp_email= 'srinadh@blackroth.in',
                                department='backend_dev',
                                salary=70000,
                                experience=5
                                
    )
    emp1 = Employee()
    emp1.add_employee(emp_obj)
    
    emp1.view_employees()
    emp1.search_employee(102)
    # emp1.update_employee(102,{'emp_name':'Atla'})
    
    # emp1.delete_employee(102)
    emp1.update_bonus()
    
    emp1.validate_employee_data()