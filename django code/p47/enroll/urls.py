from django.urls import path

from enroll import views

urlpatterns = [
    path('student/<int:my_id>/', views.show_details, name='details'),
    path('student/<int:my_id>/<int:my_sub_id>',
         views.show_sub_details,
         name='subdetails'),
    path('home/', views.home, {'check': 'OK'}, name='home'),
]
