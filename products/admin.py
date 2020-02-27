from django.contrib import admin
from .models import Perfume, CommentPerfume
# Register your models here.



admin.site.register(Perfume)
admin.site.register(CommentPerfume)


#https://djangocentral.com/creating-comments-system-with-django/

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'product', 'created_on', 'active', 'score')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'score', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)