from django.contrib import admin
from .models import Category, Forum, Thread, Reply


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'ordering', 'created_at']
    search_fields = ['name', 'description']
    ordering = ['ordering', 'name']


@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'ordering', 'thread_count', 'created_at']
    search_fields = ['title', 'description']
    list_filter = ['category', 'created_at']
    ordering = ['category', 'ordering']


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ['title', 'forum', 'author', 'is_closed', 'created_at', 'reply_count']
    search_fields = ['title', 'body', 'author__username']
    list_filter = ['forum', 'is_closed', 'created_at']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ['thread', 'author', 'created_at']
    search_fields = ['content', 'author__username', 'thread__title']
    list_filter = ['created_at']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']