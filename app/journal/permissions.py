from rest_framework import permissions


class AnonCanReadAndUserOrStaffCanCRUD(permissions.BasePermission):
    """
    Anonymous users can...
        - Lists all objects
        - Read the detail of an individual object
    Users can...
        - Lists all objects
        - See the detail of an individual object
        - Create new object
        - Update or delete object they own
    Staff can... 
        - Lists all objects
        - See the detail of an individual object
        - Cannot create new objects
        - Can update or delete any object
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return view.action == "list" or view.action == "retrieve"
        return True

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return view.action == "retrieve"

        if request.user.is_staff:
            return view.action != "create"

        return obj.user == request.user
