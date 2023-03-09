from django import forms

class BuyerForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    email = forms.EmailField()

class SellerForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    email = forms.EmailField()

class DeliveryForm(forms.Form):
    name = forms.CharField()
    number = forms.IntegerField()
    delivered = forms.BooleanField
    