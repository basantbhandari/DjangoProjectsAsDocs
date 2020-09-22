from django.shortcuts import render

from enroll.forms import StudentRegistration
# Create your views here.


def showFormData(request):
    fm = StudentRegistration()
    fm.order_fields(field_order=['email', 'name', 'first_name'])
    return render(request, 'enroll/userregistration.html', {'form': fm})
