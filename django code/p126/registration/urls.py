from django.urls import path
from registration import views
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('profile/',
         login_required(views.ProfileTemplateView.as_view()),
         name='profile'),
    # path('about/',
    #      login_required(views.AboutTemplateView.as_view()),
    #      name='about'),
    path('about/',
         staff_member_required(views.AboutTemplateView.as_view()),
         name='about'),
]
