from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'


class IsOperatorOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['admin', 'operator']


class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'employee'