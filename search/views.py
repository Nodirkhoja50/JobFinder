from django.shortcuts import render
from rest_framework.generics import ListAPIView
from work.models import Vacancy
from work.serializers import ListVacancySerializers
from .location import search_by_location,check_current_location,filter_by_location
from core.authtoken import ExpiringTokenAuthentication
# Create your views here.
class SearchVacancyListView(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = ListVacancySerializers
    authentication_classes = [ExpiringTokenAuthentication]
    def get_queryset(self,*args,**kwargs):
        latitude= self.request.GET.get('latitude')
        longitude = self.request.GET.get('longitude')
        specialty = self.request.GET.get('specialty')
        print(specialty)
        state,county = 'Toshkent','chilonzor'
        print(latitude,longitude)
        if longitude and latitude:
            coordinates = f"{latitude},{longitude}"
            state,county=check_current_location(coordinates=coordinates)
            print(state,county)
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
            results = Vacancy.objects.filter(specialty=specialty)
            results_by_location = filter_by_location(results,state,county)
        return results_by_location

search_vacancy_api = SearchVacancyListView.as_view()