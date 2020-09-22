from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Student

# from django import forms
from school.forms import StudentForm

from django.views.generic.base import TemplateView
# Create your views here.

# class StudentCreateView(CreateView):
#     model = Student
#     fields = ['name', 'email', 'password']
#     success_url = '/thanks/'

#     def get_form(self):
#         form = super().get_form()
#         form.fields['name'].widget = forms.TextInput(
#             attrs={'class': 'myclass'})
#         form.fields['password'].widget = forms.PasswordInput(
#             attrs={'class': 'myclass'})
#         return form

# class StudentUpdateView(UpdateView):
#     model = Student
#     fields = ['name', 'email', 'password']
#     success_url = '/updatethanks/'

#     def get_form(self):
#         form = super().get_form()
#         form.fields['name'].widget = forms.TextInput(
#             attrs={'class': 'myclass'})
#         form.fields['password'].widget = forms.PasswordInput(
#             attrs={'class': 'myclass'})
#         return form


class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = "school/student_form.html"
    success_url = '/thanks/'


class StudentUpdateView(UpdateView):
    model = Student
    template_name = "school/student_form.html"
    fields = ['name', 'email', 'password']
    success_url = '/updatethanks/'


class ThanksTemplateView(TemplateView):
    template_name = "school/thanks.html"


class updateThanksTemplateView(TemplateView):
    template_name = "school/updateThank.html"