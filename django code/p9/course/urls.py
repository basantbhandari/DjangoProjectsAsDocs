from django.urls import path
from course import views

urlpatterns = [path('course/', views.start_course)]
