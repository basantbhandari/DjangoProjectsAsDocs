from django.shortcuts import render
from enroll.forms import UserForm

from django.contrib import messages

# Create your views here.


def regi(request):
    if request.method == 'POST':
        fm = UserForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.info(request, 'this is info')
            messages.success(request, 'this is success')
            messages.warning(request, 'this is warning')
            messages.error(request, 'this is error')

    else:
        fm = UserForm()

    return render(request, 'enroll/userregistration.html', {'form': fm})
