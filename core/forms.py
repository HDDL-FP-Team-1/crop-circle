from django import forms
from .models import Tag, Farm, Crop, OffSite, Customer, Recipe, Ingredient, RecipeStep

class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = [
            'name',
            'website',
            'street_address',
            'street_address_line_2',
            'city',
            'state',
            'zip_code',
            'image',
        ]

class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = [
            'item'
        ]