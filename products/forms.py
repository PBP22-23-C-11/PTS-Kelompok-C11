from django import forms
from products.models import Product

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['UMKM_name', 'product_name', 'price', 'description']
        widgets = {
            'UMKM_name' : forms.TextInput(attrs={'placeholder': 'Add your UMKM name here', 'class': 'form-control rounded-lg', 'id': 'UMKM-name'}),
            'product_name' : forms.TextInput(attrs={'placeholder': 'Add your product name here', 'class': 'form-control rounded-lg', 'id': 'product-name'}),
            'price' : forms.NumberInput(attrs={'placeholder': 'Add your product price here', 'class': 'form-control rounded-lg', 'id': 'product-price'}),
            'description' : forms.Textarea(attrs={'placeholder': 'Add your description here', 'class': 'form-control rounded-lg', 'id': 'product-description'}),
        }