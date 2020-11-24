from .models import Comment1
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment1
        fields = ('name', 'email', 'body')
