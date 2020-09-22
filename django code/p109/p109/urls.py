"""p109 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from school import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',
         views.TemplateView.as_view(template_name='school/home.html'),
         name='blankhome'),
    path('home/', views.RedirectView.as_view(url='/'), name='home'),
    path('home1/', views.RedirectView.as_view(url='/something/'),
         name='home1'),
    path('index/', views.RedirectView.as_view(url='/'), name='index'),
    path('jumbotron/',
         views.RedirectView.as_view(
             url='https://getbootstrap.com/docs/4.5/components/jumbotron/'),
         name='jumbotron'),
    path('jt/',
         views.BootstrapJumboTronRedirect.as_view(),
         name='jumbotron_jt'),
    path('style/',
         views.RedirectView.as_view(pattern_name='jumbotron'),
         name='style'),
    # path('<int:id>/', views.RedirectToHome.as_view(), name='home_id'),
    path('<int:id>/',
         views.TemplateView.as_view(template_name="school/home.html"),
         name='home_id'),
]
