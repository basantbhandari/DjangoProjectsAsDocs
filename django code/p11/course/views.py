from django.shortcuts import render


# Create your views here.
def learn_python(request):
    return render(request, 'course/learn_python.html')


def learn_django(request):
    return render(request, 'course/learn_django.html')
