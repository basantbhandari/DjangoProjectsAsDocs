from django.shortcuts import render
from django.http import HttpResponse

from django.views import View

# Create your views here.


# Function based view
def myview(request):
    return HttpResponse('<h1>From function Based view</h1>')


# Class Based views
class MyView(View):
    name = 'basant'

    def get(self, request):
        # return HttpResponse('<h1>From Class based View</h1>')
        return HttpResponse(self.name)


class MyViewChild(View):
    name = 'basant'
    name1 = 'basant1'

    def get(self, request):
        # return HttpResponse('<h1>From Class based View</h1>')
        return HttpResponse(self.name)

    def post(self, request):
        return HttpResponse(self.name1)
