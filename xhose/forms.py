from django import forms
from .models import Customer


class BuyForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'phone', 'promo')
