from django.urls import path
from .views import GenerateOTP,ValidateOTP,WriteNameAPIView

urlpatterns = [
    
    path('generate', GenerateOTP.as_view(), name="generate"),
    path('validate', ValidateOTP.as_view(), name="validate"),
    path('<int:pk>/name',WriteNameAPIView.as_view(),name='write-name'),


]