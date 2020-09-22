from django.shortcuts import render
from school.models import Student
from django.db.models import Avg, Sum, Min, Max, Count


# Create your views here.
def home(request):
    student_data = Student.objects.all()
    average = student_data.aggregate(Avg('marks'))
    sum_data = student_data.aggregate(Sum('marks'))
    min_data = student_data.aggregate(Min('marks'))
    max_data = student_data.aggregate(Max('marks'))
    count_data = student_data.aggregate(Count('marks'))

    print("****************************************")
    print("Return : ", student_data)
    print("****************************************")
    print("SQL Query : ", student_data.query)
    print("****************************************")
    return render(
        request, 'school/home.html', {
            'students': student_data,
            'average': average,
            'sum': sum_data,
            'min': min_data,
            'max': max_data,
            'count': count_data,
        })
