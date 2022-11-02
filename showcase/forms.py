from django import forms
from showcase.models import Shop
from showcase.choices import CATEGORY_CHOICES

class ShopAddForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ["shop_name", "category", "description", "umkm_url", "number", "image"]

    shop_name = forms.CharField(
        label = "Name",
        required = True,
        max_length = 255,
        error_messages = {
            'required':"Please input UMKM name",
        },
        widget = forms.TextInput(
            attrs = {
                "class":"form-control",
                "id":"shop_name",
                "placeholder":"Shop's name"
            }
        )
    )

    category = forms.ChoiceField(
        label = "Category",
        required = True,
        error_messages = {
            'required':"Please select UMKM category"
        },
        widget = forms.Select(
            attrs = {
                "class":"form-control",
                "id":"category",
            }
        ),
        choices = CATEGORY_CHOICES
    )

    description = forms.CharField(
        label = "Description",
        required = True,
        error_messages = {
            "required":"Please input description"
        },
        widget = forms.Textarea(
            attrs = {
                "class":"form-control",
                "id":"description",
                "placeholder":"Shop's Description"
            }
        )
    ) 

    umkm_url = forms.URLField(
        label = "URL",
        required = True,
        error_messages = {
            "required":"Please input URL"
        }, 
        widget = forms.URLInput(
            attrs = {
                "class":"form-control",
                "id":"umkm_url",
                "placeholder":"Link"
            }
        )
    )

    number = forms.CharField(
        label = "Contact Number",
        required = True,
        max_length = 13,
        error_messages = {
            "required":"Please input UMKM's number"
        },
        widget = forms.TextInput(
            attrs = {
                "class":"form-control",
                "id":"number",
                "placeholder":"08xxxxxx"
            }
        ) 
    )

    image = forms.URLField(
        label = "Image URL",
        required = True,
        error_messages = {
            'required':"Please input image URL"
        },
        widget = forms.TextInput(
            attrs = {
                "class":"form-control",
                "id":"image",
                "placeholder":"Link to image"
            }
        )
    )

class RateForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ["rating_total"]

    rating_total = forms.IntegerField(
        label = "Rating",
        required = True,
        max_value = 5,
        min_value = 1,
        error_messages = {
            "required":"Please input rating"
        },
        widget = forms.NumberInput(
            attrs = {
                "class":"form-control",
                "id":"rating_total",
                "placeholder":"1 to 5"
            }
        )
    )