from django.contrib import admin
from school.models import Student
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    '''Admin View for Student'''

    list_display = (
        'name',
        'roll',
        'city',
        'marks',
        'passdate',
        'admdatetime',
    )
