from django.shortcuts import render
from school.models import Student

from django.views.generic.detail import DetailView

# Create your views here.


class StudentDetailView(DetailView):
    model = Student
    # template_name = "school/student.html"
    # context_object_name = 'stu'
    # pk_url_kwarg = 'id'
