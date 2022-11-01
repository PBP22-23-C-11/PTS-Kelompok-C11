from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name']
        exclude = ['user']
    first_name = forms.CharField(
        label='First Name',
        required=True,
        max_length=255,
        error_messages = {
            'required': 'Please type',
        },
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'First Name',
            }
        ),
    )
    last_name = forms.CharField(
        label='Title',
        required=True,
        max_length=255,
        error_messages = {
            'required': 'Please type',
        },
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Last Name',
            }
        ),
    )

class UMKMForm(forms.ModelForm):
    class Meta:
        model = UMKM
        fields = ['name']
        exclude = ['user']
    name = forms.CharField(
        label='Name',
        required=True,
        max_length=255,
        error_messages = {
            'required': 'Please type',
        },
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'First Name',
            }
        ),
    )