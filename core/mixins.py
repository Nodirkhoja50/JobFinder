from rest_framework import permissions
from .permission import WriteYourNamePermission
class WriteYourNamePermissionMixin():
    permission_classes = [permissions.IsAdminUser,WriteYourNamePermission]

class UserAccountSetMixin():
    user_field = "owner"

    def get_queryset(self,*args,**kwargs):
        user = self.request.user
        print(self.request.user)
        lookup_data = {}
        lookup_data[self.user_field] = user
        print(lookup_data)
        qs = super().get_queryset(*args,**kwargs)
        #print(qs)
        '''if user.is_staff:
            print(qs)
            return qs'''
        return qs.filter(**lookup_data)
