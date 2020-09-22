from django.shortcuts import render
from school.models import Student
from django.db.models import Q


# Create your views here.
def home(request):

    # student_data = Student.objects.all()[:5]
    # student_data = Student.objects.all()[5:10]
    student_data = Student.objects.all()[:10:2]

    print("****************************************")
    print("Return : ", student_data)
    print("****************************************")
    # print("SQL Query : ", student_data.query)
    print("****************************************")
    return render(request, 'school/home.html', {'students': student_data})
