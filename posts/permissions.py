from rest_framework import permissions

#for post owner
class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request,view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

#for like user
