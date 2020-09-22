from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Create your models here.
def learn_django(request):
    return HttpResponse('hay buddy')