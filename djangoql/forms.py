from django import forms
from .models import SavedQuery


class SavedQueryForm(forms.ModelForm):
    class Meta:
        model = SavedQuery
        fields = ('description', 'query', 'is_public', )
