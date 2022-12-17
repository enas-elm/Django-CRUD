from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item

        # les champs à mettre dans le formulaire
        fields = ['name', 'price', 'stock', 'image']
        
        def __init__(self):
            self.fields['image'].required = False