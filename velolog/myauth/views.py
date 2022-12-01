"""
Some docstring
"""
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import (
    LoginView as LoginViewGeneric,
    LogoutView as LogoutViewGeneric,
)
from .forms import AuthenticationForm


@login_required
def top_secret_info_view():
    """
    Some docstring
    """
    return HttpResponse("Some restricted information: ...")


class MyProfileView(TemplateView):
    """
    Some docstring
    """
    template_name = "myauth/my.html"


class LoginView(LoginViewGeneric):
    """
    Some docstring
    """
    form_class = AuthenticationForm
    next_page = reverse_lazy("myauth:my")


class LogoutView(LogoutViewGeneric):
    """
    Some docstring
    """
    next_page = reverse_lazy("myauth:my")
