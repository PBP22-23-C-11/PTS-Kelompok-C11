from django import forms
from .models import *

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'image']
        exclude = ['created_at', 'author_user']
    
    title = forms.CharField(
        label='Title',
        required=True,
        max_length=255,
        error_messages = {
            'required': 'Please type',
        },
        widget=forms.TextInput(
            attrs={
                'id': 'create-article-title',
                'class': 'form-control',
                'placeholder': 'Article Title',
            }
        ),
    )
    body = forms.CharField(
        label='Body',
        required=True,
        error_messages = {
            'required': 'Please type',
        },
        widget=forms.Textarea(
            attrs={
                'id': 'create-article-body',
                'class': 'form-control',
                'placeholder': 'Article Body',
            }
        ),
    )
    image = forms.URLField(
        label='Image',
        required=True,
        max_length=200,
        error_messages = {
            'required': 'Please type',
        },
        widget=forms.TextInput(
            attrs={
                'id': 'create-article-image',
                'class': 'form-control',
                'placeholder': 'Article Image',
            }
        ),
    )

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
                'class': 'form-control',
                'placeholder': 'Insert your comment here..',
            }
        ),
    )