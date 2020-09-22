from django.shortcuts import render
from datetime import datetime, timedelta


# Create your views here.
def set_session(request):
    request.session['name'] = 'Sonam'
    request.session['lname'] = 'Bhandari'
    return render(request, 'student/setsession.html')


def get_session(request):
    # name = request.session['name']
    name = request.session.get('name', default='Guest')
    lname = request.session.get('lname', default='Guest')
    return render(request, 'student/getsession.html', {
        'name': name,
        'lname': lname
    })


def del_session(request):
    if 'name' in request.session and 'lname' in request.session:
        del request.session['name']
        del request.session['lname']
    return render(request, 'student/delsession.html')
