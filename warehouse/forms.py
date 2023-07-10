from django import forms

from .models import Product


# Required set to false allows an empty message to be sent.
class ProductForm(forms.Form):
    note = forms.CharField(widget=forms.Textarea, required=False)
