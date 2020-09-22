from django.shortcuts import render
from django.views.decorators.cache import cache_page


# Create your views here.
# @cache_page(40)
def home(request):
    return render(request, 'enroll/course.html')


def contact(request):
    return render(request, 'enroll/contact.html')
