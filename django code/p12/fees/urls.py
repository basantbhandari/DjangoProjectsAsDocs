from django.urls import path
from fees import views
urlpatterns = [
    path('fee/', views.fee_course),
]
