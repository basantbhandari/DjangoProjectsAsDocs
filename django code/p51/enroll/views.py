from django.shortcuts import render

from enroll.forms import UserForm, TeacherForm


# Create your views here.
def student_form(request):
    if request.method == "POST":
        fm = UserForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = UserForm()
    return render(request, 'enroll/student.html', {'form': fm})


def teacher_form(request):
    if request.method == "POST":
        fm = TeacherForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = TeacherForm()
    return render(request, 'enroll/teacher.html', {'form': fm})
