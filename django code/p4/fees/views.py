from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def fees_django(request):
    return HttpResponse('Fees of Django is 3000')
