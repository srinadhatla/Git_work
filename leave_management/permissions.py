from rest_framework.permissions import BasePermission

class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and hasattr(request.user, "employee")
        )

class IsManager(BasePermission):
    def has_permission(self, request, view):
        if not hasattr(request.user, "employee"):
            return False
        employee = request.user.employee
        return (employee.designation.lower() == "manager")

class IsHR(BasePermission):
    def has_permission(self, request, view):
        if not hasattr(request.user, "employee"):
            return False
        employee = request.user.employee
        return (employee.department.name.lower() == "hr")

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff