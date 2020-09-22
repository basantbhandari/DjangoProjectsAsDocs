from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from myapp.forms import LoginForm
# Create your views here.


class MyLoginView(LoginView):
    template_name = 'myapp/login.html'
    authentication_form = LoginForm


class MyLogoutView(LogoutView):
    template_name = 'myapp/logout.html'
    authentication_form = LogoutView


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'myapp/changepassword.html'
    authentication_form = PasswordChangeView
    success_url = '/changepassworddone/'


class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'myapp/changepassworddone.html'
    authentication_form = PasswordChangeDoneView
