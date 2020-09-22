from django.shortcuts import render
from django.http import HttpResponseRedirect
from enroll.forms import StudentRegistration
# Create your views here.


def showFormData(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print(fm)
            print('from post request')
            print('CLEANED DATA = ', fm.cleaned_data)

        else:
            print('Data is not valid')

    else:
        fm = StudentRegistration()
        print('From get request')

    return render(request, 'enroll/userregistration.html', {'form': fm})
