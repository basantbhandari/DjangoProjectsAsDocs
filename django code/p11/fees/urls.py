from django.urls import path
from fees import views

urlpatterns = [
    path('python/', views.fee_python),
    path('django/', views.fee_django),
]
