from django import forms
from app.models import uploadfilemodel
from .models import Materials

class uploadfileform(forms.ModelForm):
    file = forms.FileField(widget=forms.ClearableFileInput())

    def __init__(self, *args, **kwargs):
        super(uploadfileform, self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs.update({'class': 'file', 'id': 'input-b1', 'data-browser-on-zone-click': 'true'})

    class Meta:
        model = uploadfilemodel
        fields = "__all__"
    


class DescriptionForm(forms.ModelForm):
    class Meta:
        model = Materials
        fields = ('title', 'author', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title goes Here'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Choose Author'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description goes Here'}),
        }