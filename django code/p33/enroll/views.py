from django.shortcuts import render

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
            """ 
            This is not a good way to empty the form field 
            cause initiates the resubmission
            """
        # fm = StudentRegistration()

    else:
        fm = StudentRegistration()
        print('From get request')

    return render(request, 'enroll/userregistration.html', {'form': fm})
