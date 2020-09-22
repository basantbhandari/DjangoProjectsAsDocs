from django.shortcuts import render
from datetime import datetime, timedelta


# Create your views here.
def set_session(request):
    request.session['name'] = 'Sonam'
    request.session.set_expiry(600)
    return render(request, 'student/setsession.html')


def get_session(request):
    name = request.session['name']
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    print(request.session.get_expire_at_browser_close())
    return render(request, 'student/getsession.html', {'name': name})


def del_session(request):
    request.session.flush()
    # request.session.clear_expired()
    return render(request, 'student/delsession.html')
