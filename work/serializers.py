from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Vacancy
from api.serializers import UserPublicSerializer,VacancyInlineSerializer
 
class CreateUpdateDetailVacancySerializers(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields =[
            #'owner',
            'title',
            'company_name',
            'city',
            'county',
            #location 
            'description',
            'bargain',
            'salary',
            'is_online', 
            'tg_contact',
            #"is_public",
            'created_at', 
        ]


class ListVacancySerializers(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='detail',
        lookup_field = "pk"
    )
    class Meta:
        model = Vacancy
        fields =[
            'owner',
            'url',
            'title',
            'company_name',
            #location 
            'bargain',
            'salary',
            'is_online', 
            'created_at', 
        ]
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
    
   