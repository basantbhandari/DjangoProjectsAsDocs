from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    print("I am home view")
    return render(request, 'blog/user.html')