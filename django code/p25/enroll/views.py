from django.shortcuts import render

from enroll.forms import StudentRegistration
# Create your views here.


def showFormData(request):
    #  fm = StudentRegistration(auto_id=False)
    #  fm = StudentRegistration(auto_id=True)
    #  fm = StudentRegistration(auto_id='some_%s')
    fm = StudentRegistration(auto_id="geeky",
                             label_suffix=' - ',
                             initial={
                                 'name': 'Rajesh',
                                 'email': 'rajesh@geekyshows.com'
                             })
    return render(request, 'enroll/userregistration.html', {'form': fm})
