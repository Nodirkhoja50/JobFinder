from rest_framework import serializers
from work.models import Vacancy
class FilterWorkVacancySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Vacancy
        fields = ('id','specialty',)