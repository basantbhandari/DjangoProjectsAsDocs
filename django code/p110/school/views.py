from django.shortcuts import render
from django.views.generic.list import ListView
from school.models import Student
# Create your views here.


class StudentListView(ListView):
    model = Student
