from django.urls import re_path as url
from .views import Login
from .views import Home
from .views import Index

urlpatterns = [
    url(r"home/(?P<user_id>\d+)/$",Home,name="home"),
    url(r"login/",Login,name="login"),
    url(r"",Index,name="index"),
]