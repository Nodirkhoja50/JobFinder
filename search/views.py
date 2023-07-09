from django.shortcuts import render
from rest_framework.generics import ListAPIView
from work.models import Vacancy
from work.serializers import ListVacancySerializers
# Create your views here.
class SearchVacancyListView(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = ListVacancySerializers

    def get_queryset(self,*args,**kwargs):
        qs = super().get_queryset(*args,**kwargs)
        q = self.request.GET.get('q')
        results = Vacancy.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                owner = self.request.user
            results = qs.search(q,owner=owner)
        return results

search_vacancy_api = SearchVacancyListView.as_view()