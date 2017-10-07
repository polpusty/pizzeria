from django import forms


class NewOrderForm(forms.Form):
    pizza = forms.IntegerField()


class AddPizzaToOrderForm(forms.Form):
    pizza = forms.IntegerField()


class StatusPizzaForm(forms.Form):
    status = forms.CharField()
