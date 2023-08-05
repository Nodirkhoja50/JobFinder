from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Vacancy
from api.serializers import UserPublicSerializer,VacancyInlineSerializer
from core.models import PhoneNumberAbstractUser
class CreateUpdateDetailVacancySerializers(serializers.ModelSerializer):
    owner = UserPublicSerializer(read_only=True)
    to_salary = serializers.SerializerMethodField(read_only = True)
    from_salary = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Vacancy
        fields =[
            'owner',
            'title',
            'specialty',
            'company_name',
            'city',
            'county',
            'description',
            'bargain',
            'currency',
            'from_salary',
            'to_salary',
            'is_online', 
            'tg_contact',
            #"is_public",
            'created_at', 
        ]
    def get_from_salary(self,obj):
        return obj.get_from_salary()
    

    def get_to_salary(self,obj):
        return obj.get_to_salary()

       

class ListVacancySerializers(serializers.ModelSerializer):
    '''url = serializers.HyperlinkedIdentityField(
        view_name='detail',
        lookup_field = "slug/"
    )'''
    to_salary = serializers.SerializerMethodField(read_only = True)
    from_salary = serializers.SerializerMethodField(read_only = True)
    url = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Vacancy
        fields =[
            #'owner',
            'title',
            'url',
            'description',
            'company_name',
            #location 
            'bargain',
            'currency',
            'from_salary',
            'to_salary',
            'is_online', 
            'city',
            'county',
            'created_at', 
        ]
    def get_from_salary(self,obj):
        return obj.get_from_salary()
    

    def get_to_salary(self,obj):
        return obj.get_to_salary()

    def get_url(self,obj):
            return obj.get_absolute_url()
    
class UpdatePublicVacancySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Vacancy
        fields = [
            "id",
            "is_public",
            ]



class MyAccountSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(read_only = True)
    related_vacancy = VacancyInlineSerializer(source = 'owner.vacancy_set.all',read_only=True,many=True)
    
    class Meta:
        model = Vacancy
        fields = [
            "owner",
            #"title",
            "related_vacancy",
            #"edit_url",
            #"create_url",
            #"is_public_url",
            #'created_at',
            ]
    

class ListFavoriteSerializer(serializers.ModelSerializer):
    favorites = ListVacancySerializers(many=True, read_only=True)

    class Meta:
        model = PhoneNumberAbstractUser
        fields = ['id', 'favorites']