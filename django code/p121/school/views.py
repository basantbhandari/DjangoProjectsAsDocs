from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Student

from school.forms import StudentForm

from django.views.generic.base import TemplateView


class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = "school/student_form.html"
    success_url = '/thanks/'


class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/create/'


class StudentUpdateView(UpdateView):
    model = Student
    template_name = "school/student_form.html"
    fields = ['name', 'email', 'password']
    success_url = '/updatethanks/'


class ThanksTemplateView(TemplateView):
    template_name = "school/thanks.html"


class updateThanksTemplateView(TemplateView):
    template_name = "school/updateThank.html"