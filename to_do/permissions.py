from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """ Check owner or admin """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user or request.user.is_staff
