from django.shortcuts import render
from enroll.models import Student


# Create your views here.
def base(request):
    stud = Student.objects.all()
    return render(request, 'enroll/base.html', {'stu': stud})