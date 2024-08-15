from rest_framework import permissions


class IsActiveUser(permissions.BasePermission):
    """Проверка на активного пользователя"""

    def has_object_permission(self, request, view, obj):
        return request.user.is_active
