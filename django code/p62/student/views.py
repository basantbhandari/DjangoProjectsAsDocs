from django.shortcuts import render
from datetime import datetime, timedelta


# Create your views here.
def setcookie(request):
    response = render(request, "student/setcookies.html")
    response.set_signed_cookie("name",
                               "sonam",
                               salt="nm",
                               expires=datetime.utcnow() + timedelta(days=2))
    return response


def getcookie(request):
    name = request.get_signed_cookie('name', default="Guest", salt="nm")
    return render(request, 'student/getcookies.html', {'name': name})


def delcookie(request):
    response = render(request, 'student/delcookies.html')
    response.delete_cookie('name')
    return response