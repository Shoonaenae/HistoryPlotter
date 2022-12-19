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
        fields = ('title', 'author', 'project', 'period', 'description', 'actual_material')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title goes Here'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Choose Author'}),
            'project': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Choose Project'}),
            'period': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date in History'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description goes Here'}),
            'actual_material': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title goes Here'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Materials
        fields = ('title', 'description' )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title goes Here'}),
            #'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Choose Author'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description goes Here'}),
        }