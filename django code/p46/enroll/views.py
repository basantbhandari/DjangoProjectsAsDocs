from django.shortcuts import render
from django.http import HttpResponseRedirect
from enroll.forms import StudentRegistration

from .models import User

# Create your views here.


def showFormData(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            # nm = fm.cleaned_data['name']
            # em = fm.cleaned_data['email']
            # pw = fm.cleaned_data['password']
            # to create new column
            # reg = User(name=nm, email=em, password=pw)
            # reg.save()
            # to update the created value
            # reg = User(id=1, name=nm, email=em, password=pw)
            # reg.save()
            # to delete the created value
            reg = User(id=1)
            reg.delete()

        else:
            print('Data is not valid')

    else:
        fm = StudentRegistration()
        print('From get request')

    return render(request, 'enroll/userregistration.html', {'form': fm})
