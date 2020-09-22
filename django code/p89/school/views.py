from django.shortcuts import render

from .models import Student, Teacher
from django.db.models import Q
# Create your views here.


def home(request):
    student_data = Student.objects.all()
    # student_data = Student.objects.filter(marks=67)
    # student_data = Student.objects.exclude(marks=67)
    # student_data = Student.objects.order_by('marks')
    # student_data = Student.objects.order_by('-marks')
    # student_data = Student.objects.order_by('?')

    # student_data = Student.objects.order_by('-marks').reverse()
    # student_data = Student.objects.order_by('-marks').reverse()[:5]
    # student_data = Student.objects.values()
    # student_data = Student.objects.values('name', 'city')

    # student_data = Student.objects.using('default')
    # student_data = Student.objects.dates('pass_date', 'year')
    # student_data = Student.objects.dates('pass_date', 'month')

    #######################  Second Tables 'Teacher' Started ###############################

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs2.union(qs1)

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs2.union(qs1, all=True)

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs2.intersection(qs1)

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs2.difference(qs1)

    ##################### AND or OR OPERATOR ####################
    # student_data = Student.objects.filter(id=1) & Student.objects.filter(
    #     roll=1)
    # student_data = Student.objects.filter(id=1, roll=1)
    # student_data = Student.objects.filter(Q(id=1) & Q(roll=1))

    # student_data = Student.objects.filter(id=1) | Student.objects.filter(
    #     roll=2)
    # student_data = Student.objects.filter(Q(id=1) | Q(roll=2))

    print("Return : ", student_data)
    print("Return SQL Query : ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})
