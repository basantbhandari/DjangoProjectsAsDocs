from django.contrib import admin
from school.models import Student, Teacher, Contractor
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    '''Admin View for Student'''

    list_display = ('name', 'age', 'date', 'fees')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    '''Admin View for Teacher'''

    list_display = ('name', 'age', 'date', 'salary')


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    '''Admin View for Contractor'''

    list_display = ('name', 'age', 'date', 'payment')
