from django import forms

from cosplay_project.store.models import Items


class ItemCreateFrom(forms.ModelForm):
    class Meta:
        model = Items
        exclude = ('user',)
