from django.shortcuts import render
from school.models import Student

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.


class StudentDetailView(DetailView):
    model = Student


class StudentListView(ListView):
    model = Student
