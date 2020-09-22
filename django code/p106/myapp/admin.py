from django.contrib import admin
from .models import Page, Post, Song


# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    '''Admin View for Page'''

    list_display = ('page_name', 'page_cat', 'page_publish_date', 'user')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = ('post_title', 'post_cat', 'post_publish_date', 'user')


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    '''Admin View for Song'''

    list_display = ('song_name', 'song_duration', 'written_by')
