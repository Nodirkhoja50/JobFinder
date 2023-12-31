from rest_framework.permissions import BasePermission
class WriteYourNamePermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        endpoint_id = view.kwargs.get('pk')
        print(view.kwargs)
        if user.id != endpoint_id:
            return False
        return bool(request.user and request.user.is_authenticated)

