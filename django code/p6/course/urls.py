from django.urls import path
from course import views
urlpatterns = [
    path('django/', views.learn_django),
    path('python/', views.learn_python),
]
