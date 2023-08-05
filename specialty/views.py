# specialty/views.py
# specialty/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Specialty
from .serializers import SpecialtySerializer
from core.authtoken import ExpiringTokenAuthentication
from core.models import PhoneNumberAbstractUser
from core.serializers import SelectSpecialtySerializer
from rest_framework.generics import UpdateAPIView,ListAPIView
from django.shortcuts import get_object_or_404
from work.models import Vacancy
from rest_framework import status
class SpecialtyListAPIView(APIView):
    #queryset = Vacancy.specialty.field.choices
    #serializer_class = SpecialtySerializer
    #authentication_classes = [ExpiringTokenAuthentication]
    '''def get(self, request):
        choices = 'None'
        language = self.request.headers.get('Accept-Language', 'en')
        if language == "uz":
            choices = Specialty.Uz_Status.choices
        if language == "ru":
            choices = Specialty.Ru_Status.choices
        choices = Specialty.objects.all()
        #choices_dict = {key: value for key, value in choices}
        choices = SpecialtySerializer(choices,many = True)
        print(type(choices))
        return Response(choices)'''
    def get(self, request):
        language = self.request.headers.get('Accept-Language', 'en')
        serializer = SpecialtySerializer()
        data = {"data": serializer.to_representation(language)}
        return Response(data)



class SelectSpecialtyAPIView(UpdateAPIView):
    queryset = PhoneNumberAbstractUser.objects.all()
    serializer_class = SelectSpecialtySerializer
    
    authentication_classes = [ExpiringTokenAuthentication]
    lookup_field = "pk"  

    def get_object(self):
        user = self.request.user
        obj = get_object_or_404(PhoneNumberAbstractUser, phone_number=user.phone_number)
        self.check_object_permissions(self.request, obj)

        return obj

    def perform_update(self, serializer):
        language = self.request.headers.get('Accept-Language', 'en')
        specialty_key = serializer.validated_data.get('specialty')
        if specialty_key:
            try:
                choice = 'None'
                
                if language == "uz":
                    choice = Specialty.Uz_Status(specialty_key)
                if language == "ru":
                    choice = Specialty.Ru_Status(specialty_key)           
                if specialty_key:
                    serializer.save(specialty=specialty_key)
                    response = {
                        "specialty":choice  
                    }
                    return Response(response, status=status.HTTP_200_OK)
            except ValueError:
                return Response({"error": "Invalid specialty key"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Specialty key not provided"}, status=status.HTTP_400_BAD_REQUEST)

select_specialty_api = SelectSpecialtyAPIView.as_view()
