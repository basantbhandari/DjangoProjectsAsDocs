from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse


# Create your views here.
def home(request):
    print("I am home view")
    return HttpResponse("This is home page")


def exception_view(request):
    print("I am from exception view")
    a = 10 / 0
    return HttpResponse("This is home page")


def user_info(request):
    print("I am from user info view")
    context = {'name': 'Rahul'}
    return TemplateResponse(request, 'blog/user.html', context)
