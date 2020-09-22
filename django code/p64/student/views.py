from django.shortcuts import render
from datetime import datetime, timedelta


# Create your views here.
def set_session(request):
    request.session['name'] = 'Sonam'
    return render(request, 'student/setsession.html')


def get_session(request):
    name = request.session.get('name', default='Guest')
    keys = request.session.keys()
    items = request.session.items()
    # age = request.session.setdefault('age', '30')
    return render(
        request,
        'student/getsession.html',
        {
            'name': name,
            'keys': keys,
            'items': items,
            # 'age': age
        })


def del_session(request):
    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush()
    return render(request, 'student/delsession.html')
