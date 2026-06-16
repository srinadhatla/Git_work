import json
class EmployeeAPI:
    def __init__(self):
        self.load_data()
        
    def load_data(self):
        try:
            with open('employee_management_system/data/users.json','r') as file_obj:
                val = file_obj.read()
            if val:
                self.employee_data = json.loads(val)
            else:
                self.employee_data = []
                print("All data",self.employee_data)
        except FileNotFoundError:
            print("file not found")
        except:
            print("file got error")
            
    def save_data(self):
        with open('employee_management_system/data/users.json','w') as file_obj:
            file_obj.write(json.dumps(self.employee_data))
        print("file got saved")
        
    def add_employee(self,emp_id,name,salary,department):
        current_user_dict = {'emp_id':emp_id, 'emp_name':name,'salary':salary,'department':department}
        print(self.employee_data)
        self.employee_data.append(current_user_dict)
        self.save_data()
    
    
    def get_employee(self):
        # for emp_info in self.employee_data:
        #     print("Employee ID:", emp_info['emp_id'])
        #     print("Employee name:", emp_info['emp_name'])
        #     print("Salary:", emp_info['salary'])
        #     print("Department:", emp_info['department'])
        return self.employee_data
            
    def get_employee_by_id(self,emp_id):
        for emp_info in  self.employee_data:
            if emp_info['emp_id'] == emp_id:
                print("Employee ID:", emp_info['emp_id'])
                print("Employee name:", emp_info['emp_name'])
                print("Salary:", emp_info['salary'])
                print("Department:", emp_info['department'])
                return emp_info
                break
            else:
                print("employee not found")
                
    def delete_employee(self,emp_id):
        for index,emp_info in self.employee_data:
            if emp_info['emp_id'] == emp_id:
                self.employee_data.pop(index)
                break
            print(self.employee_data)
        self.save_data()
            
    def calculate_bonus(self,experience,salary):
        if experience<=2:
            bonus = salary*0.02
        elif experience<=5:
            bonus = salary*0.10
        elif experience>=5:
            bonus = salary*0.20
        return bonus
    
    def update_employee(self,updated_employee_info):
        for emp_info in self.employee_data:
            if emp_info['emp_id'] == emp_info:
                self.update(updated_employee_info)
                break
            else:
                print("ID not found")
        print("Data Updated")
        print(self.employee_data)
        self.save_data()
            
    def updated_bonus(self):
        for emp_info in self.employee_data:
            bonus = self.calculate_bonus(emp_info['salary'], emp_info['department'])
            self.update_employee(emp_info['emp_id'], {'bonus': bonus})
            print("Employee ID:", emp_info['emp_id'])
            print("Employee Name:", emp_info['emp_name'])
            print("Employee Salary:", emp_info['salary'])
            print("Employee experience:", emp_info['experience'])
        
    
    
    def duplicate_emp_id(self):
        employee_Id = []
        duplicate_id = []
        for emp_info in self.employee_data:
            if emp_info.get('emp_id') not in employee_Id:
                employee_Id.append(emp_info.get('emp_id'))
            else:
                duplicate_id.append(emp_info.get('emp_id'))
        if duplicate_id:
            print("Duplicate id found", duplicate_id)
       