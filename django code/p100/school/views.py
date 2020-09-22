from django.shortcuts import render
from school.models import Student


# Create your views here.
def home(request):
    # student_data = Student.students.all()
    # student_data = Student.students.all()
    student_data = Student.students.get_stu_roll_range(40, 105)
    return render(request, 'school/home.html', {'students': student_data})
