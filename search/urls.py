from django.urls import path
from .views import search_vacancy_api
from filter.views import FilterWorkVacancyAPIView
urlpatterns = [
    path("list/",search_vacancy_api,name='search'),
    #path("list/",FilterWorkVacancyAPIView.as_view())
]