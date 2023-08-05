from django.urls import path,include
from .views import FilterWorkVacancyAPIView
urlpatterns = [
    path('list/',FilterWorkVacancyAPIView.as_view(),name='filter-work')
]