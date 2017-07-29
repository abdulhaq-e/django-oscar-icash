from django import forms


class iCashForm(forms.Form):
    icard = forms.IntegerField()
    paycode = forms.IntegerField()
    
    