from django.urls import path
from .views import SpecialtyListAPIView,SelectSpecialtyAPIView
app_name = 'specialty'
urlpatterns = [
 path('specialty',SpecialtyListAPIView.as_view(),name='get-specialty'),
 path('user/specialty',SelectSpecialtyAPIView.as_view(),name='put-specialty')
]