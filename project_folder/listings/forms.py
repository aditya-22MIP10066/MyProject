# D:\Coding arena\python_codes\project_folder\listings\forms.py
from django import forms
from .models import ItemListing

class ItemListingForm(forms.ModelForm):
    class Meta:
        model = ItemListing
        fields = ['name', 'description', 'quantity', 'price', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}), # Make textarea larger
        }