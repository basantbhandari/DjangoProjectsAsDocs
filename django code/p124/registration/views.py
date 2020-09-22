from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.
@login_required
def ProfileView(request):
    return render(request, 'registration/profile.html')


# @login_required
@staff_member_required
def AboutView(request):
    return render(request, 'registration/about.html')
