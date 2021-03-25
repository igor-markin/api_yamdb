from django.contrib import admin
from .models import User, Review, Comment

admin.site.register(User)


@admin.register(Review)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'text', 'created', 'author')
    search_fields = ('text',)
    list_filter = ('created',)
    empty_value_display = '-empty-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'text', 'created', 'author')
    search_fields = ('text',)
    list_filter = ('created',)
    empty_value_display = '-empty-'
