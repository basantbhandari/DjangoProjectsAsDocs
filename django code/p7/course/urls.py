from django.urls import path

from . import views

urlpatterns = [
    path('python/', views.learn_python),
    path('django/', views.learn_django),
]
