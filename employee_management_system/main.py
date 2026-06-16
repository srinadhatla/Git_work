from services.employee_manager import Employee
from models.employee import employeeBaseModel
from models.users import userBaseModel


if __name__ == "__main__":
    emp_obj = employeeBaseModel(
                                emp_id=103,
                                emp_name= 'srinadhreddy',
                                emp_email= 'srinadh@blackroth.in',
                                department='backend_dev',
                                salary=70000,
                                experience=5,
                                emp_role='Admin'                     
    )
    
    user_ob = userBaseModel(emp_id=101,emp_role='Hr')
    emp1 = Employee()
    # emp1.add_employee(user_ob,emp_obj)
    
    # emp1.view_employees(user_ob)
    # emp1.search_employee(user_ob,102)
    emp1.update_employee(user_ob,101,{'emp_name':'Atla'})
    
    # emp1.delete_employee(user_ob,102)
    # emp1.update_bonus()
    
    # emp1.validate_employee_data()