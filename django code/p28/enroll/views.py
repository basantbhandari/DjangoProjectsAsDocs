from django.shortcuts import render

from enroll.forms import StudentRegistration
# Create your views here.


def showFormData(request):
    fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form': fm})
