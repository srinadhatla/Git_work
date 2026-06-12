def validate_duplicate_emp(employee_data):
    employee_id = []
    duplicate_id = []
    for emp_info in employee_data:
        if emp_info.get('emp_id') not in employee_id:
            employee_id.append(emp_info.get('emp_id'))
        else:
            duplicate_id.append(emp_info.get('emp_id'))

    if duplicate_id:
        print("Duplicate ID found",duplicate_id)