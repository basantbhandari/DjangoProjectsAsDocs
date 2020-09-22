from django.shortcuts import render
from datetime import datetime, timedelta


# Create your views here.
def settestcookie(request):
    print(request.session.set_test_cookie())
    return render(request, 'student/settestcookie.html')


def checktestcookie(request):
    print(request.session.test_cookie_worked())
    return render(request, 'student/checktestcookie.html')


def deltestcookie(request):
    print(request.session.delete_test_cookie())
    return render(request, 'student/delcookie.html')
