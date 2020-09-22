from django.shortcuts import render
from enroll.forms import UserForm

from django.contrib import messages

# Create your views here.


def regi(request):
    if request.method == 'POST':
        fm = UserForm(request.POST)
        if fm.is_valid():
            fm.save()
            # messages.add_message(request, messages.SUCCESS,
            #                      'Your Account has been created !!!')
            messages.success(request, 'Your account has been created !!!')
            messages.info(request, 'Your account has been created !!!')

    else:
        fm = UserForm()

    return render(request, 'enroll/userregistration.html', {'form': fm})
