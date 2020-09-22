from django.shortcuts import render
from school.models import Student

from datetime import date, time


# Create your views here.
def home(request):
    student_data = Student.objects.all()

    # student_data = Student.objects.filter(name__exact='basant123')
    # student_data = Student.objects.filter(name__iexact='Basant123')

    # student_data = Student.objects.filter(name__contains='A')
    # student_data = Student.objects.filter(name__icontains='A')

    # student_data = Student.objects.filter(id__in=[1, 5, 7, 9])

    # student_data = Student.objects.filter(marks__gt=60)
    # student_data = Student.objects.filter(marks__lt=60)

    # student_data = Student.objects.filter(marks__gte=60)
    # student_data = Student.objects.filter(marks__lte=60)

    # student_data = Student.objects.filter(name__startswith='b')
    # student_data = Student.objects.filter(name__istartswith='b')

    # student_data = Student.objects.filter(name__endswith='a')
    # student_data = Student.objects.filter(name__iendswith='3')

    # student_data = Student.objects.filter(passdate__range=('2020-04-01',
    #                                                        '2020-10-30'))

    # student_data = Student.objects.filter(admdatetime__date=date(2020, 10, 1))
    # student_data = Student.objects.filter(
    #     admdatetime__date__lte=date(2020, 10, 1))

    # student_data = Student.objects.filter(passdate__year=2020)
    # student_data = Student.objects.filter(passdate__year__gte=2019)

    # student_data = Student.objects.filter(passdate__month=4)
    # student_data = Student.objects.filter(passdate__month__gte=4)

    # student_data = Student.objects.filter(passdate__day=20)
    # student_data = Student.objects.filter(passdate__day__gte=20)

    # student_data = Student.objects.filter(passdate__week=20)
    # student_data = Student.objects.filter(passdate__week__lte=20)

    # student_data = Student.objects.filter(passdate__week_day=6)
    # student_data = Student.objects.filter(passdate__week_day__gt=3)

    # student_data = Student.objects.filter(passdate__quarter=3)
    # student_data = Student.objects.filter(passdate__quarter__gt=3)

    # student_data = Student.objects.filter(admdatetime__time__gt=time(6, 00))
    # student_data = Student.objects.filter(admdatetime__hour__gt=5)
    # student_data = Student.objects.filter(admdatetime__minute__gt=5)
    # student_data = Student.objects.filter(admdatetime__second__gt=5)
    # student_data = Student.objects.filter(roll__isnull=False)

    print("****************************************")
    print("Return : ", student_data)
    print("****************************************")
    print("SQL Query : ", student_data.query)
    print("****************************************")
    return render(request, 'school/home.html', {'students': student_data})
