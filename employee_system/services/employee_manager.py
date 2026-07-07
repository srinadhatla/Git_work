from utils.helper import load_data, save_data,calculate_bonus
from utils.validator import validate_duplicate_emp

class Employee:
    def __init__(self):
        self.employee_data = load_data()

    def add_employee(self,model_obj):
        self.employee_data.append(dict(model_obj))
        save_data(self.employee_data)
    
    def view_employees(self):
        for emp_info in self.employee_data:
            print("Employee ID:", emp_info['emp_id']) # emp_info.get('emp_id',"0000")
            print("Employee Name:", emp_info['emp_name'])
            print("Employee Salary:", emp_info['salary'])
            print("Employee experience:", emp_info['experience'])
            print("*****************************************")
            
            
    def update_bonus(self):
        for emp_info in self.employee_data:
            bonus = calculate_bonus(emp_info['experience'],emp_info['salary'])
            self.update_employee(emp_info['emp_id'],{'bonus':bonus})
            print("Employee ID:", emp_info['emp_id'])
            print("Employee Name:", emp_info['emp_name'])
            print("Employee Salary:", emp_info['salary'])
            print("Employee experience:", emp_info['experience'])
            
    def search_employee(self,emp_id):
        for emp_info in self.employee_data:
            if emp_info['emp_id'] == emp_id:
                print("Employee ID:", emp_info['emp_id'])
                print("Employee Name:", emp_info['emp_name'])
                print("Employee Salary:", emp_info['salary'])
                print("Employee experience:", emp_info['experience'])
                
                break
        else:
            print("Employee ID is not found")
    def update_employee(self,emp_id,updated_employee_info):
        for emp_info in self.employee_data:
            if emp_info['emp_id'] == emp_id:
                emp_info.update(updated_employee_info)
                break
        else:
            print("Employee ID is not found")
        print("Updated Data")
        print(self.employee_data)
        save_data(self.employee_data)
    def delete_employee(self, emp_id):
        for index,emp_info in enumerate(self.employee_data):
            if emp_info['emp_id'] == emp_id:
                self.employee_data.pop(index)
                break
        print(self.employee_data)
        save_data(self.employee_data)
        
    def save_employee_data(self):
        save_data(self.employee_data)
        
    def validate_employee_data(self):
        validate_duplicate_emp(self.employee_data)
