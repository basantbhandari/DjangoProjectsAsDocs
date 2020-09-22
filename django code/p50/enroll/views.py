from django.shortcuts import render

from enroll.forms import UserForm

# Create your views here.


def showFormData(request):
    fm = UserForm()
    return render(request, 'enroll/userregistration.html', {'form': fm})
