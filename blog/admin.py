from django.contrib import admin

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['label', 'short_description', 'full_description', 'user']
    search_fields = ['label', 'user']
    ordering = ['label']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ['username', 'text', 'for_post', 'is_published']
    search_fields = ['username', 'for_post']
    ordering = ['is_published']
