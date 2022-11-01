from django import forms

class AddProductForm(forms.Form):
    UMKM_name = forms.CharField(label="UMKM Name", max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Add your UMKM name here', 'class': 'form-control rounded-lg h-10 pl-4 w-full', 'id': 'UMKM-name'}))
    product_name = forms.CharField(label="Product Name", max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Add your product name here', 'class': 'form-control rounded-lg h-10 pl-4 w-full', 'id': 'product-name'}))
    price = forms.IntegerField(label="Product Price", required=True, widget=forms.NumberInput(attrs={'placeholder': 'Add your product price here', 'class': 'form-control rounded-lg h-10 pl-4 w-full', 'id': 'product-price'}))
    description = forms.CharField(label="Product Description", required=True, widget=forms.Textarea(attrs={'placeholder': 'Add your description here', 'class': 'form-control rounded-lg h-10 pl-4 w-full', 'id': 'product-description'}))