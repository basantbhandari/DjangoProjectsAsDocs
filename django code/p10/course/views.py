from django.shortcuts import render


# Create your views here.
def learn_one(request):
    return render(request, 'course/courseone.html')


def learn_two(request):
    return render(request, 'course/coursetwo.html')
