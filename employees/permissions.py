from rest_framework.permissions import BasePermission


class ReadOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        return request.method == 'GET'

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.userprofile.role == 'admin')


class IsHR(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.userprofile.role == 'HR')


class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.userprofile.role == 'employee')