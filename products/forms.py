from django import forms

class AddProductForm(forms.Form):
    UMKM_name = forms.CharField(label="UMKM Name", 
                            widget=forms.TextInput(attrs={'placeholder': 'Enter your UMKM name'}))
    product_name = forms.CharField(label="Product Name", 
                            widget=forms.TextInput(attrs={'placeholder': 'Enter your product name'}))
    price = forms.IntegerField(label="Product Price",
                                widget=forms.TextInput(attrs={'placeholder': 'Enter your product price'}))
    description = forms.CharField(label="Description", required=False,
                                    widget=forms.Textarea(attrs={'placeholder': 'Tell us about yout product'}))