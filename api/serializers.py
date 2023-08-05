from rest_framework import serializers
from rest_framework.reverse import reverse

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only = True)
    phone_number = serializers.CharField(read_only=True) 
    id = serializers.IntegerField(read_only = True)

class VacancyInlineSerializer(serializers.Serializer):
    title = serializers.CharField(read_only = True)
   
    is_public_url = serializers.SerializerMethodField(read_only =True)

    '''edit_url = serializers.HyperlinkedIdentityField(
        view_name='update',
        lookup_field = "pk"
    )'''
    
    
    create_url = serializers.SerializerMethodField(
        read_only = True
        )
    created_at = serializers.DateTimeField(read_only=True)
    
    def get_create_url(self,obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("work:create",request=request)
    
    def get_is_public_url(self,obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("work:make-private",request=request)
    