from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Student
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
# from django import forms

from school.forms import StudentForm

# Create your views here.

# class StudentCreateView(CreateView):
#     model = Student
#     template_name = "school/home.html"
#     fields = ['name', 'email', 'password']
#     success_url = '/thanks/'

#     def get_form(self):
#         form = super().get_form()
#         form.fields['name'].widget = forms.TextInput(
#             attrs={'class': 'myclass'})
#         form.fields['password'].widget = forms.PasswordInput(
#             attrs={'class': 'myclass'})
#         return form


class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = "school/home.html"
    success_url = '/thanks/'


class ThankyouTemplateView(TemplateView):
    template_name = "school/thanks.html"


class StudentDetailView(DetailView):
    model = Student
    template_name = "school/details.html"
