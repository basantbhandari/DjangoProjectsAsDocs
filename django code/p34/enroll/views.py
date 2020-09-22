from django.shortcuts import render
from django.http import HttpResponseRedirect
from enroll.forms import StudentRegistration
# Create your views here.


def thankyou(request):
    return render(request, 'enroll/success.html')


def showFormData(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print(fm)
            print('from post request')
            print('CLEANED DATA = ', fm.cleaned_data)
            """
            This reder is suitable for not changing in URL
            """
            # return render(request, 'enroll/success.html', {'nm': fm})
            """
                Alternative method is 
            """
            return HttpResponseRedirect('/enroll/success/')

        else:
            print('Data is not valid')

    else:
        fm = StudentRegistration()
        print('From get request')

    return render(request, 'enroll/userregistration.html', {'form': fm})
