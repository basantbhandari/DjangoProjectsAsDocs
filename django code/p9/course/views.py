from django.shortcuts import render

# Create your views here.


def start_course(request):
    frotend_stuff = {'course': 'Django'}
    return render(request, 'course/course.html', context=frotend_stuff)