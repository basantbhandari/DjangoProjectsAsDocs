from django.shortcuts import render, HttpResponse
from datetime import datetime, timedelta


# Create your views here.
def set_session(request):
    request.session['name'] = 'Sonam'
    return render(request, 'student/setsession.html')


def get_session(request):
    if 'name' in request.session:
        name = request.session['name']
        request.session.modified = True
        return render(request, 'student/getsession.html', {'name': name})
    else:
        return HttpResponse('Your session get expired')


def del_session(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'student/delsession.html')
