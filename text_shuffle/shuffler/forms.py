from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(label="Select text file")

    def clean_file(self):
        uploaded_file = self.cleaned_data['file']

        if not uploaded_file.name.endswith('.txt'):
            raise forms.ValidationError("File must have .txt extension")

        if uploaded_file.content_type != 'text/plain':
            raise forms.ValidationError("File must be a text type")

        return uploaded_file
