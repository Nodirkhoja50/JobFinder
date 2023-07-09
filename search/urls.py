from django.urls import path
from .views import search_vacancy_api
urlpatterns = [
    path("api/",search_vacancy_api,name='create')
]