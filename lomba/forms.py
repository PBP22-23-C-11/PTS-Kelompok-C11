from django import forms
from lomba.models import Lomba

# Define the class for the customer form
class LombaForm(forms.ModelForm):
    class Meta:
        model = Lomba
        fields = ['namaLomba', 'keterangan']
        exclude = ['tanggal']
    
    namaLomba = forms.CharField(
        label = 'Nama Lomba',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
            }
        ),
    )

    keterangan = forms.CharField(
        label = 'Keterangan',
        widget = forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        ),
    )