# specialty/serializers.py
from rest_framework import serializers
from .models import Specialty
from work.models import Vacancy
from rest_framework import serializers

class SpecialtySerializer(serializers.Serializer):
    key = serializers.CharField()
    value = serializers.CharField()

    def to_representation(self, language):
        # Access the choices directly from the model
        choices = Specialty.Uz_Status.choices
        print(language)
        if language == "uz":
            choices = Specialty.Uz_Status.choices
        if language == "ru":
            choices = Specialty.Ru_Status.choices
        

        # Return a list of dictionaries with 'key' and 'value' fields
        return [{"key": key, "value": value} for key, value in choices]
