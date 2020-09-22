from django.urls import path
from fees import views

urlpatterns = [
    path('learnone/', views.learn_one),
    path('learntwo/', views.learn_two),
]