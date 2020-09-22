from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def learn_django_fee(request):
    return HttpResponse('Learn django')


def learn_python_fee(request):
    return HttpResponse('Learn python')
