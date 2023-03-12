from rest_framework.permissions import BasePermission



class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True



class IsSuperUserORStaffReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser or request.user.is_staff:
            return True



class IsSuperUserOrOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or request.user == obj:
            return True