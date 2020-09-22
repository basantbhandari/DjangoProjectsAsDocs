from django.shortcuts import render
from django.http import HttpResponseRedirect
from enroll.forms import StudentRegistration

# Create your views here.


def showFormData(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            print(nm)
            print(em)
            print(pw)

        else:
            print('Data is not valid')

    else:
        fm = StudentRegistration()
        print('From get request')

    return render(request, 'enroll/userregistration.html', {'form': fm})
