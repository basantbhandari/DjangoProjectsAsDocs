from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def fee_django(request):
    return HttpResponse('fee of django')


def fee_python(request):
    return HttpResponse('fee of python')
