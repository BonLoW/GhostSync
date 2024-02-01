from django.urls import path
from django.urls import re_path
from .views import *

urlpatterns = [
    path("login/", Login, name="login"),
    path("home/", Home, name="home"),
    path("index/", Index, name="index"),
    path("",Index,name="default"),
]