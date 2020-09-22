from django.contrib import admin
from school.models import ExamCenter, MyExamCenter

# Register your models here.


@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    '''Admin View for ExamCenter'''

    list_display = ('id', 'cname', 'city')


@admin.register(MyExamCenter)
class MyExamCenterAdmin(admin.ModelAdmin):
    '''Admin View for MyExamCenter'''

    list_display = ('id', 'cname', 'city')
