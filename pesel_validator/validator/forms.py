from django import forms
from .validation import validate_pesel


class PeselForm(forms.Form):

    pesel = forms.CharField(
        min_length=11,
        max_length=11,
        label="PESEL",
        widget=forms.TextInput(attrs={"pattern": "[0-9]*", "inputmode": "numeric", "maxlength": "11", "minlength": "11"}),)

    def clean_pesel(self):
        pesel = self.cleaned_data['pesel']
        result = validate_pesel(pesel)

        self.cleaned_data['result'] = result

        return pesel
