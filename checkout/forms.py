from django import forms
from .models import Customer, OrderLineItem

class CustomerPaymentForm(forms.Form):
    """creditcard payment"""
    MONTH_CHOICES = [(i,i)for i in range(1,12)]
    YEAR_CHOICES = [(i,i)for i in range(2020, 2040)]

    credit_card_number = forms.CharField(label='Card Number', required=False)
    cvv = forms.CharField(label='Security Code (cvv)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    
class CustomerShippingForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'phone_number','street_address','postcode','county','country')


