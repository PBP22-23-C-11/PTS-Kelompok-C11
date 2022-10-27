from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        exclude = ['user', 'article']
    
    body = forms.CharField(
        label='Body',
        required=True,
        max_length=255,
        error_messages = {
            'required': 'Please type',
        },
        widget=forms.Textarea(
            attrs={
                'id': 'comment_body',
                'class': 'test',
                'placeholder': 'Insert your comment here..',
            }
        ),
    )