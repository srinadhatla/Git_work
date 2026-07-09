from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return(request.user.is_authenticated and request.user.role == "Admin")
    
class IsHR(BasePermission):
    def has_permission(self, request, view):
        return(request.user.is_authenticated and request.user.role == "HR")
    
class IsManager(BasePermission):
    def has_permission(self, request, view):
        return(request.user.is_authenticated and request.user.role == "Manager")
    
class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return(request.user.is_authenticated and request.user.role == "Employee")
    
class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user