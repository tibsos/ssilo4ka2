from django.urls import path

from .views import *

urlpatterns = [

    path('register', register),
    path('register2', register2),

]