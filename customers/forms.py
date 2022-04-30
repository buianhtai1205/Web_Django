from django import forms
from .models import Customer

class CreateCustomersForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'email', 'password', 'phone', 'address')