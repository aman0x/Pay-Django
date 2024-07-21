from rest_framework import permissions

class IsOwnerOrAdder(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow access if the user is the owner or the adder of the account
        return obj.user == request.user or obj.added_by == request.user
