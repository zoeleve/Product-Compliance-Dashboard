from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "ADMIN"


class IsManufacturer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ("ADMIN", "MANUFACTURER")


class IsViewer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if request.user.role == "ADMIN":
            return True
        owner = getattr(obj, "manufacturer", getattr(obj, "user", None))
        return owner == request.user
