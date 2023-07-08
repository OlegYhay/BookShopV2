from django import forms

from mainapp.models import Order


class OrderCustomForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'secondname', 'email', 'fulladdress', 'notification', 'Payment']
