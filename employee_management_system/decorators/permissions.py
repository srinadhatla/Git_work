from functools import wraps

def autherization(func):
    @wraps(func)
    def wrapper(*args):
        if args[1].emp_role == 'Admin':
            func(*args)
        elif args[1].emp_role == 'Hr' and func.__name__ != 'delete_employee':
            func(*args)
        elif args[1].emp_role == 'Employee' and func.__name__ in ('search_employee','view_employees'):
            print(args)
            func(*args)
        else:
            print("user doesnot have permissions")
    return wrapper
