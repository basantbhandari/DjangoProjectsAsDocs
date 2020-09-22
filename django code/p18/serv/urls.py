from django.urls import path
from serv import views

urlpatterns = [
    path('services/', views.services, name='services'),
]
