from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import PhoneToken,PhoneNumberAbstractUser
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User

class PhoneTokenCreateSerializer(ModelSerializer):
    phone_number = serializers.CharField(validators =PhoneNumberField().validators)

    class Meta:
        model = PhoneToken
        fields = ('pk','phone_number')

class PhoneTokenValidateSerializer(ModelSerializer):
    pk = serializers.IntegerField()
    otp  = serializers.CharField(max_length = 40)

    class Meta:
        model = PhoneToken
        fields = ('pk','otp')

class WriteUserNameSerializer(ModelSerializer):
    username = serializers.CharField(max_length=50)
    class Meta:
        model = PhoneNumberAbstractUser
        fields = ('username',)




