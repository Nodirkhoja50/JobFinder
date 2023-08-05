from django.shortcuts import render

# Create your views here.
from work.models import Vacancy
from .serializers import FilterWorkVacancySerializer
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from core.authtoken import ExpiringTokenAuthentication

from work.serializers import ListVacancySerializers
class FilterWorkVacancyAPIView(ListAPIView):
    queryset = Vacancy
    serializer_class = ListVacancySerializers
    authentication_classes = [ExpiringTokenAuthentication]
    def get_queryset(self):
        specialty=self.request.query_params.get('specialty')
        print(specialty)
        filtered_vancancy = Vacancy.objects.filter(specialty=specialty)
        return filtered_vancancy