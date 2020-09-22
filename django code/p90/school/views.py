from django.shortcuts import render

from .models import Student
# Create your views here.


def home(request):
    # student_data = Student.objects.get(pk=1)
    # student_data = Student.objects.first()
    # student_data = Student.objects.order_by('-name').first()

    # student_data = Student.objects.last()
    # student_data = Student.objects.order_by('-name').last()
    # student_data = Student.objects.latest('pass_date')
    # student_data = Student.objects.earliest('pass_date')

    # student_data = Student.objects.all()
    # print("exist :", student_data.exists())

    # student_data = Student.objects.all()
    # one_data = Student.objects.get(pk=1)
    # print(student_data.filter(pk=one_data.pk).exists())

    # student_data = Student.objects.create(name='Sameer',
    #                                       roll=112,
    #                                       city='Bokaro',
    #                                       marks=60,
    #                                       pass_date='2020-5-4')

    # student_data, created = Student.objects.get_or_create(name='Sameer',
    #                                                       roll=112,
    #                                                       city='Bokaro',
    #                                                       marks=60,
    #                                                       pass_date='2020-5-4')
    # print(student_data, created)

    # student_data = Student.objects.filter(id=2).update(name='kabir', marks=80)

    # student_data, created = Student.objects.update_or_create(
    #     id=2, name='kabir', defaults={'name': 'Sameer_updated'})

    # student_data, created = Student.objects.update_or_create(
    #     id=20,
    #     name='kabira',
    #     defaults={
    #         'name': 'Kabir_created',
    #         'roll': '23',
    #         'city': 'Kathmandu',
    #         'marks': 76,
    #         'pass_date': '2020-5-4'
    #     })

    # print("Created : ", created)

    # objs = [
    #     Student(name='Sonam',
    #             roll=120,
    #             city='Dhanbad',
    #             marks=40,
    #             pass_date='2020-5-4'),
    #     Student(name='Sonam1',
    #             roll=1201,
    #             city='Dhanbad1',
    #             marks=401,
    #             pass_date='2020-5-4'),
    #     Student(name='Sonam2',
    #             roll=1202,
    #             city='Dhanbad2',
    #             marks=402,
    #             pass_date='2020-5-5'),
    #     Student(name='Sonam3',
    #             roll=1203,
    #             city='Dhanbad3',
    #             marks=403,
    #             pass_date='2020-5-6'),
    #     Student(name='Sonam4',
    #             roll=1204,
    #             city='Dhanbad4',
    #             marks=404,
    #             pass_date='2020-5-7'),
    # ]

    # student_data = Student.objects.bulk_create(objs)

    # all_student_data = Student.objects.all()
    # for stu in all_student_data:
    #     stu.city = 'Bhel'

    # student_data = Student.objects.bulk_update(all_student_data, ['city'])

    # student_data = Student.objects.in_bulk([1, 2])
    # print(student_data[1].name)
    # print()
    # student_data1 = Student.objects.in_bulk([])
    # print(student_data1)
    # print()
    # student_data2 = Student.objects.in_bulk()
    # print(student_data2)

    # student_data = Student.objects.get(pk=2)
    # deleted = student_data.delete()

    # student_data = Student.objects.filter(marks=404).delete()

    # student_data = Student.objects.all()
    # print(student_data.count())

    print(Student.objects.all().explain())
    student_data = {}
    print("Return : ", student_data)
    return render(request, 'school/home.html', {'student': student_data})
