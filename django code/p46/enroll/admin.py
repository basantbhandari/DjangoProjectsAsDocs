from django.contrib import admin
from .models import User

# Register your model here


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')