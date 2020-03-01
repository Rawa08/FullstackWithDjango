from django.contrib import admin
from .models import Comment
# Register your models here.

admin.site.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'post', 'created_on', 'score', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'text', 'score')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
