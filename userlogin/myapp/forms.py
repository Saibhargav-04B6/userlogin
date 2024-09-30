from django import forms
from .models import Product
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','type','value']
    def clean_price(self):
        price=self.cleaned_data.get('price')
        if(price<0):
            raise forms.ValidationError('Price must be positive')
        return price
        