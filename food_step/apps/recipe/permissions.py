from rest_framework import permissions


class LoginRequiredPermission(object):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated()


class RecipePermission(LoginRequiredPermission, permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return True if request.method in permissions.SAFE_METHODS else\
            request.user == obj.user


class ChildRecipePermission(LoginRequiredPermission,
                            permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return True if request.method in permissions.SAFE_METHODS else\
            request.user == obj.recipe.user
