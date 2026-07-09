from rest_framework.permissions import BasePermission

class IsHRorAdmin(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return(request.user.is_staff or request.user.groups.filter(name="HR").exits())
    
    
class IsDocumentOwnerOrHR(BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.user.is_staff:
            return True

        if request.user.groups.filter(name="HR").exists():
            return True

        return (obj.employee.user == request.user)