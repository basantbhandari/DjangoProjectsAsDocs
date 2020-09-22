from django.shortcuts import render
from school.models import Student

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.


class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["all_student"] = self.model.objects.all().order_by('name')
        return context


class StudentListView(ListView):
    model = Student
