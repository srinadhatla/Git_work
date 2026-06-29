from employees.models import Employee


class EmployeeRepository:

    @staticmethod
    def get_all():
        return Employee.objects.select_related("department").all()

    @staticmethod
    def get_by_id(id):
        return Employee.objects.select_related("department").get(id=id)

    @staticmethod
    def create(data):
        return Employee.objects.create(**data)

    @staticmethod
    def update(employee, data):
        for key, value in data.items():
            setattr(employee, key, value)
        employee.save()
        return employee

    @staticmethod
    def delete(employee):
        employee.delete()