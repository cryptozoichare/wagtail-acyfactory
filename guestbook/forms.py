# forms.py
from django import forms
from .models import GuestbookEntry

class GuestbookForm(forms.ModelForm):
    class Meta:
        model = GuestbookEntry
        fields = ['name', 'message']
