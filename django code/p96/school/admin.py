from django.contrib import admin
from school.models import ExamCenter, Student


# Register your models here.
@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    '''Admin View for ExamCenter'''

    list_display = ('cname', 'city')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    '''Admin View for Student'''

    list_display = ('name', 'roll')
