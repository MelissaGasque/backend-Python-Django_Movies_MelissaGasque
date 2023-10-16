from rest_framework import permissions
from rest_framework.views import Request, View


class IsAdminOrAuthenticated(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        if request.method == 'PATCH':
            if request.user.is_authenticated:
                if request.user.is_superuser:
                    return True
                user_id = view.kwargs.get('user_id')
                if request.user.id == user_id:
                    return True
            return False
        
        if request.method == 'GET':
            if request.user.is_authenticated:
                if request.user.is_superuser:
                    return True
                user_id = view.kwargs.get('user_id')
                if request.user.id == user_id:
                    return True
            return False

        return False