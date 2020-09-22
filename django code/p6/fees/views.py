from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def fee_django(request):
    return HttpResponse('Learning the django has fee 6000')


def fee_python(request):
    return HttpResponse('Learning the python has fee 8000')
