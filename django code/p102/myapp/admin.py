from django.contrib import admin

from myapp.models import Page
# Register your models here.


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    '''Admin View for Page'''

    list_display = ('user', 'page_name', 'page_cat', 'page_publish_date')
