from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (create_vacancy_api,
                    list_vacancy_api,
                    make_private_vacancy,
                    udpate_vacancy_api,
                    detail_vacancy_api,
                    my_account_api,
                    AddFavoriteView,
                    RemoveFavoriteView,
                    ListFavoriteView)
app_name = 'work'
urlpatterns = [
    path("auth",obtain_auth_token),
    path("create",create_vacancy_api,name='create'),
    path("list/",list_vacancy_api,name="list"),
    #path("detail/<int:pk>",detail_vacancy_api,name="detail"),
    path("list/<slug:vacancy>/<int:pk>",detail_vacancy_api,name='detial'),
    path("update/<int:pk>",udpate_vacancy_api,name='update'),
    path("myaccount",my_account_api,name="account"),
    path("myaccount/edit/makeprivate",make_private_vacancy,name='make-private'),
    path('add-favourite/<int:pk>', AddFavoriteView.as_view(), name='add_favorite'),
    path('remove-favourite/<int:pk>',RemoveFavoriteView.as_view()),
    path('list-favourite',ListFavoriteView.as_view())
    #path("make_vacancy_private/<int:owner>/<int:id>",MakePrivate.as_view()),
] 