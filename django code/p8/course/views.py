from django.shortcuts import render

# Create your views here.


def learn_python(request):
    return render(request, 'course/coursepython.html')


def learn_django(request):
    return render(request, 'course/coursedjango.html')