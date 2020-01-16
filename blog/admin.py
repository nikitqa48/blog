from django.contrib import admin
from .models import Post, Comment
# Register your models here.
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','body','publish','created','updated','status','id']
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

@admin.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'name', 'email', 'body', 'created', 'update', 'active']
    list_filter = ('post', 'created', 'update')
    search_fields = ('name', 'post', 'created', 'update', 'email')
    date_hierarchy = 'created'
    ordering = ['update', 'created']