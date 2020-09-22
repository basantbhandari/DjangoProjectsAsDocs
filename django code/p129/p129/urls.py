"""p129 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from myapp.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',
         TemplateView.as_view(template_name='myapp/home.html'),
         name='home'),
    path('dashboard/',
         TemplateView.as_view(template_name='myapp/dashboard.html'),
         name='dashboard'),
    path('login/',
         auth_views.LoginView.as_view(
             template_name='myapp/login.html',
             authentication_form=LoginForm,
         ),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='myapp/logout.html'),
         name='logout'),
    path('changepassword/',
         auth_views.PasswordChangeView.as_view(
             template_name='myapp/changepassword.html',
             success_url='/changepassworddone/'),
         name='changepassword'),
    path('changepassworddone/',
         auth_views.PasswordChangeView.as_view(
             template_name='myapp/changepassworddone.html'),
         name='changepassworddone'),
]
