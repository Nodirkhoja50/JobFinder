from typing import Any, Dict
from django.shortcuts import render
from rest_framework import status
from django.views import View
from rest_framework.generics import (CreateAPIView,
                                     ListAPIView,
                                     UpdateAPIView,
                                     RetrieveAPIView,
                                     GenericAPIView)
from api.paginations import CustomPagination
from core.mixins import UserAccountSetMixin
from .models import Vacancy
from django.http import HttpResponse
from search.location import list_by_location,check_current_location,search_by_location,filter_by_location
from core.authtoken import ExpiringTokenAuthentication
from .serializers import (CreateUpdateDetailVacancySerializers,
                          ListVacancySerializers,
                          UpdatePublicVacancySerializer,
                          MyAccountSerializer,
                          ListFavoriteSerializer)
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from core.models import PhoneNumberAbstractUser
class CreateVacancyAPIView(CreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = CreateUpdateDetailVacancySerializers
    authentication_classes = [ExpiringTokenAuthentication]
    permission_classes = []

    def perform_create(self, serializer):
        slug = None
        #salary = serializer.validated_data.get('salary')
        #print(salary)
        #print(type(salary))
        #barging = serializer.validated_data.get('bargain')
        title = serializer.validated_data.get('title')
        title = serializer.validated_data.get('from_salary')
        if title:
            slug = title.lower().replace(' ', '-')  
        #salary = Vacancy.is_negotiable(salary,barging) 
            serializer.save(owner = self.request.user,slug = slug)
        else:
            return Response("something went wrong")
create_vacancy_api = CreateVacancyAPIView.as_view()


class ListVacancyAPIView(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = ListVacancySerializers
    pagination_class = CustomPagination
    authentication_classes = [ExpiringTokenAuthentication]
    permission_classes = []
    #queryset = queryset.offset(2).limit(10)
   

    
    '''def get_queryset(self):
        latitude= self.request.GET.get('latitude')
        longitude = self.request.GET.get('longitude')
        state,county = 'Toshkent','chilonzor'
        if longitude and latitude:
            coordinates = f"{latitude},{longitude}"
            state,county=check_current_location(coordinates=coordinates)
            print(state,county)
        user = self.request.user
        if user:
            specialty = user.specialty
        return list_by_location(specialty,state,county)'''
    def get_queryset(self,*args,**kwargs):
        user = self.request.user
        latitude= self.request.GET.get('latitude')
        longitude = self.request.GET.get('longitude')
        specialty = self.request.GET.get('specialty')
        state,county = 'Toshkent','chilonzor'
        #print(latitude,longitude)
        if longitude and latitude:
            coordinates = f"{latitude},{longitude}"
            state,county=check_current_location(coordinates=coordinates)
            #print(state,county)
        qs = super().get_queryset(*args,**kwargs)
        q = self.request.GET.get('q')
        results = Vacancy.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                owner = self.request.user
            results = qs.search(q,owner=owner)
            results_by_location = search_by_location(results,state,county)
            #print(results_by_location)
        elif specialty is not None:
            if self.request.user.is_authenticated:
                owner = self.request.user
                print(owner , 'OWNER')
            results = qs.specialty(specialty)#,owner=owner
            ''' print(type(specialty))
            print(specialty)
            results = Vacancy.objects.filter(specialty=specialty)'''
            results_by_location = filter_by_location(results,state,county)

        elif specialty and q:
            if self.request.user.is_authenticated:
                owner = self.request.user
                print(owner , 'OWNER')
            results = qs.search_inside_specialty(q,specialty,owner=owner)
            results_by_location = filter_by_location(results,state,county)
        else:
             if self.request.user.is_authenticated:
                owner = self.request.user
                specialty = user.specialty
                results = qs.list_by_public(owner)
                results_by_location = list_by_location(results,specialty,state,county)
        return results_by_location
        
            



list_vacancy_api = ListVacancyAPIView.as_view()


from django.db.models import Count

class DetailVacancyAPIView(RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = CreateUpdateDetailVacancySerializers
    #authentication_classes = [ExpiringTokenAuthentication]
    lookup_field = "pk"
    def get_serializer_context(self):
        post = self.get_object()
        similar_vacancy = Vacancy.objects.filter(specialty = post.specialty).exclude(id=post.id)
        similar_vacancy1 = similar_vacancy.annotate(same_specialty = Count('specialty')).order_by('-created_at')
        print(similar_vacancy1)
        #return Response(ListVacancySerializers(similar_vacancy).data)
detail_vacancy_api = DetailVacancyAPIView.as_view()


class UpdateVacancyAPIView(UpdateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = CreateUpdateDetailVacancySerializers
    authentication_classes = []#ExpiringTokenAuthentication
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
    authentication_classes = []#ExpiringTokenAuthentication
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
    authentication_classes = [ExpiringTokenAuthentication]
    #authentication_classes = [SessionAuthentication]
    permission_classes = []
    lookup_field = "pk"

my_account_api = MyAccountAPIView.as_view()

''''class LikedVacancyAPIView(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = 
    authentication_classes = [ExpiringTokenAuthentication]
    lookup_field = 'pk'''''



class AddFavoriteView(CreateAPIView):
    #queryset = PhoneNumberAbstractUser.objects.all()
    #serializer_class = OwnerSerializer
    authentication_classes = [ExpiringTokenAuthentication]
    
    def post(self, request, *args, **kwargs):
        owner = self.request.user
        vacancy_id = self.kwargs.get('pk')  # Assuming vacancy_id is provided in the POST request data
        try:
            vacancy = Vacancy.objects.get(pk=vacancy_id)
        except Vacancy.DoesNotExist:
            return Response({'error': 'Vacancy not found'}, status=status.HTTP_404_NOT_FOUND)

        owner.favorites.add(vacancy)
        return Response({"msg":"added"},status=status.HTTP_200_OK)
        #return Response(self.get_serializer(owner).data, status=status.HTTP_200_OK)
    
class RemoveFavoriteView(UpdateAPIView):
    authentication_classes = [ExpiringTokenAuthentication]

    def put(self, request, *args, **kwargs):
        owner = self.request.user
        vacancy_id = self.kwargs.get('pk')  # Assuming vacancy_id is provided in the POST request data
        try:
            vacancy = Vacancy.objects.get(pk=vacancy_id)
        except Vacancy.DoesNotExist:
            return Response({'error': 'Vacancy not found'}, status=status.HTTP_404_NOT_FOUND)

        owner.favorites.remove(vacancy)
        return Response({"msg":"removed"},status=status.HTTP_200_OK)

class ListFavoriteView(ListAPIView):
    queryset = PhoneNumberAbstractUser.objects.all()
    serializer_class = ListFavoriteSerializer
    authentication_classes = [ExpiringTokenAuthentication]
    def get(self, request, *args, **kwargs):
        owner = self.request.user
        return Response(self.get_serializer(owner).data, status=status.HTTP_200_OK)
