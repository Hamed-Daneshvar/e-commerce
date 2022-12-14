from dataclasses import fields
from socket import fromshare
from django import forms
from localflavor.us.forms import USZipCodeField
from .models import Order

class OrderCreationForm(forms.ModelForm):
    postal_code = USZipCodeField()
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 
                  'address', 'postal_code', 'city',]