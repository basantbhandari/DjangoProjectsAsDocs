from django.shortcuts import render, HttpResponseRedirect
from enroll.forms import StudentRegistrationForm
from enroll.models import StudentRegistration

# Create your views here.


def add_show(request):
    """ This function will Add new Item and Show All Items """

    if request.method == 'POST':
        fm = StudentRegistrationForm(request.POST)
        if fm.is_valid():
            # fm.save()
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']

            reg = StudentRegistration(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistrationForm()

    else:
        fm = StudentRegistrationForm()

    stud = StudentRegistration.objects.all()

    return render(request, 'enroll/addstudent.html', {'form': fm, 'stu': stud})


def deleteItem(request, id):
    """ This function will deletes the colume identified """
    if request.method == 'POST':
        pi = StudentRegistration.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/enroll/add/')


def updateItem(request, id):
    """ This function will update and display  """
    if request.method == "POST":
        pi = StudentRegistration.objects.get(pk=id)
        fm = StudentRegistrationForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = StudentRegistration.objects.get(pk=id)
        fm = StudentRegistrationForm(instance=pi)

    return render(request, 'enroll/updatestudent.html', {'form': fm})
