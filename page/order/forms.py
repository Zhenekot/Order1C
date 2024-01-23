from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['count', 'product', 'client', 'placeImpl', 'car', 'placeFrom']

        def __init__(self, *args, **kwargs):
            super(OrderForm, self).__init__(*args, **kwargs)
            self.fields['product'].widget.attrs.update({'list': 'products'})
            self.fields['client'].widget.attrs.update({'list': 'clients'})
            self.fields['placeImpl'].widget.attrs.update({'list': 'placesImpl'})
            self.fields['car'].widget.attrs.update({'list': 'cars'})
            self.fields['placeFrom'].widget.attrs.update({'list': 'placesFrom'})
