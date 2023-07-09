from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.generics import CreateAPIView,UpdateAPIView
from django.contrib.auth import authenticate,login
from rest_framework.response import Response
from .models import PhoneToken,PhoneNumberAbstractUser
from .serializers import (
    PhoneTokenCreateSerializer, PhoneTokenValidateSerializer,WriteUserNameSerializer
)
from .utils import user_detail
from .mixins import WriteYourNamePermissionMixin


class GenerateOTP(CreateAPIView):
    queryset = PhoneToken.objects.all()
    serializer_class = PhoneTokenCreateSerializer
    

    def post(self, request, format=None):
        # Get the patient if present or result None.
        ser = self.serializer_class(
            data=request.data,
            context={'request': request}
        )


        
        #what is outputing in this is like:::::PhoneTokenCreateSerializer(context={'request': <rest_framework.request.Request: POST '/generate'>}, data=<QueryDict: {'csrfmiddlewaretoken': ['w03ed63DvHlpJdiq1IV7KyUAVzkc1IfJ6LUKXc9JTdgtXiDoSbqVMMvU6hooIzD5'], 'phone_number': ['+998978824042']}>):
                                               #pk = IntegerField(label='ID', read_only=True)
                                               #phone_number = CharField(validators=[<function validate_international_phonenumber>, <django.core.validators.MaxLengthValidator object>]

        if ser.is_valid():
            token = PhoneToken.create_otp_for_numbers(
                request.data.get('phone_number')
                
            )

           
            #there is token :::: +998978824042-304358
             
            if token:
                phone_token = self.serializer_class(
                    token, context={'request': request}
                )

                
                #this is phone token::::PhoneTokenCreateSerializer(<PhoneToken: +998978824042-304358>, context={'request': <rest_framework.request.Request: POST '/generate'>}):
                                        #pk = IntegerField(label='ID', read_only=True)
                                        #phone_number = CharField(validators=[<function validate_international_phonenumber>, <django.core.validators.MaxLengthValidator object>])

                data = phone_token.data

          
                #this is data {'pk': 46, 'phone_number': '+998978824042'}

                if getattr(settings, 'PHONE_LOGIN_DEBUG', False):
                    data['debug'] = token.otp
                return Response(data)
            return Response({
                'reason': "you can not have more than {n} attempts per day, please try again tomorrow".format(
                    n=getattr(settings, 'PHONE_LOGIN_ATTEMPTS', 10))}, status=status.HTTP_403_FORBIDDEN)
        return Response(
            {'reason': ser.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)


class ValidateOTP(CreateAPIView):
    queryset = PhoneToken.objects.all()
    serializer_class = PhoneTokenValidateSerializer
    
    def post(self, request, format=None):
        # Get the patient if present or result None.
        ser = self.serializer_class(
            data=request.data, context={'request': request}
        )
        if ser.is_valid():
            pk = request.data.get("pk")
            otp = request.data.get("otp")
            try:
                user = authenticate(request,pk=pk,otp=otp)
                
                if user:
                    last_login = user.last_login

                login(request,user)
                response = user_detail(user, last_login)
                return Response(response, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response(
                    {'reason': "OTP doesn't exist"},
                    status=status.HTTP_406_NOT_ACCEPTABLE
                )
        return Response(
            {'reason': ser.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
    
class WriteNameAPIView(WriteYourNamePermissionMixin,UpdateAPIView):
    queryset = PhoneNumberAbstractUser.objects.all()
    serializer_class = WriteUserNameSerializer
    lookup_field = 'pk'
    def perform_update(self, serializer):
        instance = serializer.save()
        
    

















