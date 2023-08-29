from django import forms
from book.models import Product

class PriceFilter(forms.Form):
    start_price = forms.IntegerField(widget=forms.NumberInput(attrs={'value': '0'}))
    end_price = forms.IntegerField(widget=forms.NumberInput(attrs={'value': Product.objects.latest('price').price}))

