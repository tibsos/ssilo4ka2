from django.urls import path

from .views import *

urlpatterns = [

    path('<str:username>/', profile),

    path('al', add-link) # add link
    path('el', edit-link) # edit link
    path('dl', delete-link) # delete link

]