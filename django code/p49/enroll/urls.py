from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('add/', views.add_show, name='addandshow'),
    path('update/<int:id>', views.updateItem, name='update'),
    path('delete/<int:id>', views.deleteItem, name='delete'),
]