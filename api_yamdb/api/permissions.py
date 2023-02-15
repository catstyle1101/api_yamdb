from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """
    полные права на управление всем контентом проекта. Доступ - only Админ
    """
    def has_object_permission(self, request, view, obj):
        return (request.user.is_authenticated and (
            request.user.is_admin or request.user.is_superuser))
         

class IsAdminReadOnly(permissions.BasePermission):
    """ 
    пользователя с правами admin
    """
    def has_object_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated and (
            request.user.is_admin or request.user.is_superuser))


class IsModeratorAdminAuthorOrReadOnly(permissions.BasePermission):
    """"
    Модератор те же права, что и у Аутентифицированного пользователя,
    плюс право удалять и редактировать любые отзывы и комментарии.
    """
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)
    
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_admin
                or request.user.is_moderator
                or obj.author == request.user)
