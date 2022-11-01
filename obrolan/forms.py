from django import forms
from .models import Diskusi
from django.contrib.auth.models import User

class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Diskusi
        fields=['title', 'message']

        title = forms.CharField(max_length=100)
        message = forms.Textarea()

        widgets = {
            'title' : forms.TextInput(attrs={'placeholder': 'Default <Reply>'}),
            'message' : forms.Textarea(attrs={'rows': 4}),
        }