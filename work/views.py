from django.shortcuts import render
from rest_framework.generics import (CreateAPIView,
                                     ListAPIView,
                                     UpdateAPIView,
                                     RetrieveAPIView,
                                     GenericAPIView)
from api.paginations import CustomPagination
from core.mixins import UserAccountSetMixin
from .models import Vacancy
from core.authtoken import ExpiringTokenAuthentication
from .serializers import (CreateUpdateDetailVacancySerializers,
                          ListVacancySerializers,
                          UpdatePublicVacancySerializer,
                          MyAccountSerializer)
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication

class CreateVacancyAPIView(CreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = CreateUpdateDetailVacancySerializers
    #authentication_classes = [ExpiringTokenAuthentication]
    permission_classes = []

    def perform_create(self, serializer):
        
        salary = serializer.validated_data.get('salary')
        barging = serializer.validated_data.get('bargain')

        salary = Vacancy.is_negotiable(salary,barging) 
        if salary:
            serializer.save(owner = self.request.user,salary = salary)
        else:
            return Response("something went wrong")
create_vacancy_api = CreateVacancyAPIView.as_view()


class ListVacancyAPIView(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = ListVacancySerializers
    #pagination_class = CustomPagination
    #authentication_classes = []
    permission_classes = []


    def get(self, request, *args, **kwargs):
        print(self.get_serializer)
        return Response(" ")
            



list_vacancy_api = ListVacancyAPIView.as_view()



class DetailVacancyAPIView(RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = CreateUpdateDetailVacancySerializers
    lookup_field = "pk"

detail_vacancy_api = DetailVacancyAPIView.as_view()


class UpdateVacancyAPIView(UpdateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = CreateUpdateDetailVacancySerializers
    authentication_classes = [ExpiringTokenAuthentication]
    permission_classes = []
    lookup_field = "pk"    

    
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def perform_update(self, serializer):
        serializer.save()
    

udpate_vacancy_api = UpdateVacancyAPIView.as_view()



class MakePrivateVacancyAPIView(UpdateAPIView):

    queryset = Vacancy.objects.all()
    serializer_class = UpdatePublicVacancySerializer
    authentication_classes = [ExpiringTokenAuthentication]
    permission_classes = []


    def put(self, request, *args, **kwargs):
        data = request.data
        ser = self.serializer_class(
            data=data,
            context={'request': request},
            many=isinstance(request.data, list)
        )
        ser.is_valid(raise_exception=True)
        if isinstance(data,list): #Update multiple elements
            for elm in ser.validated_data:
                Vacancy.update_is_public(elm)
        else: #Update one element
            Vacancy.update_is_public(ser.validated_data)
        return Response({"msg":"updateted"})

    def get(self, request):
        serialized = self.serializer_class(self.get_queryset(), many=True)
        return Response(serialized.data)

make_private_vacancy = MakePrivateVacancyAPIView.as_view()


class MyAccountAPIView(UserAccountSetMixin,ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = MyAccountSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = []
    lookup_field = "pk"

my_account_api = MyAccountAPIView.as_view()