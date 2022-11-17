from django import forms
from app.models import uploadfilemodel

class uploadfileform(forms.ModelForm):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    def __init__(self, *args, **kwargs):
        super(uploadfileform, self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs.update({'class': 'file', 'id': 'input-b1', 'data-browser-on-zone-click': 'true'})

    class Meta:
        model = uploadfilemodel
        fields = "__all__"