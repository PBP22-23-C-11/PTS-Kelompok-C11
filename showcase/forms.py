from django import forms
from showcase.models import Shop

class ShopAddForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ["shop_name", "description", "umkm_url", "number"]
        exclude = ["owner", "rating_count", "rating_total"]

        shop_name = forms.CharField(
            label = "shop_name",
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

        description = forms.CharField(
            label = "description",
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
            label = "umkm_url",
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
            label = "number",
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

class RateForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ["rating_count"]

    rating_count = forms.IntegerField(
        label = "rating_count",
        required = True,
        max_value = 5,
        error_messages = {
            "required":"Please input rating"
        },
        widget = forms.NumberInput(
            attrs = {
                "class":"form-control",
                "id":"rating_count",
                "placeholder":"1 to 5"
            }
        )
    )