from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('book_title', 'slug', 'status', 'created_on')
    search_fields = ['book_title']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('book_title',)}
    summernote_fields = ('content',)

# Register your models here.

admin.site.register(Comment)