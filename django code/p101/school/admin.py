from django.contrib import admin
from school.models import Student, ProxyStudent


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    '''Admin View for Student'''

    list_display = ('id', 'name', 'roll')


@admin.register(ProxyStudent)
class ProxyStudentAdmin(admin.ModelAdmin):
    '''Admin View for ProxyStudent'''

    list_display = ('id', 'name', 'roll')
