from django.contrib import admin

from enroll.models import StudentRegistration
# Register your models here.


@admin.register(StudentRegistration)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')
