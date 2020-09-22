from django.urls import path
from fees import views
urlpatterns = [
    path('django/', views.fee_django),
    path('python/', views.fee_python),
]
