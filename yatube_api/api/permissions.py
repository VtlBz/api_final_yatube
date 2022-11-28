from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    message = 'Запрещено изменение и/или удаление чужого контента!'

    # def has_object_permission(self, request, view, obj):
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
    #     return obj.author == request.user

    # Можно, но нужно ли?
    # Тем более в одну строку всё равно не лезет...

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
