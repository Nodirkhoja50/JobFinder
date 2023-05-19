from django.urls import path
from .views import GenerateOTP,ValidateOTP

urlpatterns = [
    path('generate', GenerateOTP.as_view(), name="generate"),
    path('validate', ValidateOTP.as_view(), name="validate"),
    #path('validate',my_post_api)
]