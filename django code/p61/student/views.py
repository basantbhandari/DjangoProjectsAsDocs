from django.shortcuts import render
from datetime import datetime, timedelta


# Create your views here.
def setcookie(request):
    response = render(request, "student/setcookies.html")
    # response.set_cookie("name", "sonam")
    # response.set_cookie("name", "sonam", max_age=10)
    response.set_cookie("name",
                        "sonam",
                        expires=datetime.utcnow() + timedelta(days=2))
    return response


def getcookie(request):
    # name = request.COOKIES['name']
    # name = request.COOKIES.get('name')
    name = request.COOKIES.get('name', 'Guest')
    return render(request, 'student/getcookies.html', {'name': name})


def delcookie(request):
    response = render(request, 'student/delcookies.html')
    response.delete_cookie('name')
    return response