import json

def calculate_bonus(experience,salary):
    if experience<=2:
        bonus = salary * 0.05
    elif experience<=5:
        bonus = salary * 0.10
    elif experience>5:
        bonus = salary * 0.20
    return bonus


def save_data(employee_data):
    with open('data/employees.json','w') as file_obj:
        file_obj.write(json.dumps(employee_data))
    print("File data got saved")


def load_data():
    try:
        employee_data =  None
        with open('data/employees.json','r') as file_obj:
            file_data = file_obj.read()
            if file_data:
                employee_data =  json.loads(file_data)
                print("loaded........")
                print("All data", employee_data)
            else:
                return []
                
        return employee_data
    except FileNotFoundError:
        print('File Not found')
    except:
        print("got unexpected error")