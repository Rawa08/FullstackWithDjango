from .models import CommentPerfume
from django import forms

#https://djangocentral.com/creating-comments-system-with-django/
class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentPerfume
        fields = ('name', 'body', 'score')