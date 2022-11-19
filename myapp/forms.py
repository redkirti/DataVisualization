from django import forms
from .models import Document

class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a file')
    tag = forms.CharField(max_length = 100, label='Enter Name for the file')
