from django.urls import path
from course import views

urlpatterns = [
    path('', views.course, name='courseinfo'),
]