from django.shortcuts import render, HttpResponse
from datetime import datetime, timedelta


# Create your views here.
def set_session(request):
    request.session['name'] = 'Sonam'
    return render(request, 'student/setsession.html')


def get_session(request):
    name = request.session['name']
    return render(request, 'student/getsession.html', {'name': name})


def del_session(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'student/delsession.html')
