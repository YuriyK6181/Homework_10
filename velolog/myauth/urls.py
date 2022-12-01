"""
Some docstring
"""
from django.urls import path
from .views import MyProfileView, LoginView, LogoutView, top_secret_info_view

APP_NAME = "myauth"

urlpatterns = [
    path("secret/", top_secret_info_view, name="hidden"),
    path("my/", MyProfileView.as_view(), name="my"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]