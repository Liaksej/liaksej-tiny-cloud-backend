from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user.user == request.user


class IsOwnerOrStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user.user == request.user or request.user.is_staff
