from django.shortcuts import render

# Create your views here.


def home(request, check):
    return render(request, 'enroll/home.html', {'ck': check})


# def show_details(request, my_id):
#     if my_id == 1:
#         student = {'id': my_id, 'name': 'Rohan'}
#     if my_id == 2:
#         student = {'id': my_id, 'name': 'Raj'}
#     if my_id == 3:
#         student = {'id': my_id, 'name': 'Simran'}
#     if my_id == 4:
#         student = {'id': my_id, 'name': 'Arora'}
#     return render(request, 'enroll/show.html', student)


def show_details(request, my_id=1):
    if my_id == 1:
        student = {'id': my_id, 'name': 'Rohan'}
    if my_id == 2:
        student = {'id': my_id, 'name': 'Raj'}
    if my_id == 3:
        student = {'id': my_id, 'name': 'Simran'}
    if my_id == 4:
        student = {'id': my_id, 'name': 'Arora'}
    return render(request, 'enroll/show.html', student)


def show_sub_details(request, my_id, my_sub_id):
    if my_id == 1 and my_sub_id == 1:
        student = {
            'id': my_id,
            'name': 'Rohan',
            'info': 'hay buddy from sub student'
        }
    if my_id == 2 and my_sub_id == 2:
        student = {
            'id': my_id,
            'name': 'Raj',
            'info': 'hay buddy from sub student'
        }
    if my_id == 3 and my_sub_id == 3:
        student = {
            'id': my_id,
            'name': 'Simran',
            'info': 'hay buddy from sub student'
        }
    if my_id == 4 and my_sub_id == 4:
        student = {
            'id': my_id,
            'name': 'Arora',
            'info': 'hay buddy from sub student'
        }
    return render(request, 'enroll/show.html', student)
