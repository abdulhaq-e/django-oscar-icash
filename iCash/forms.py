from django import forms


class iCashForm(forms.Form):
    
    icard_no = forms.CharField()
    confirmation_code = forms.IntegerField()
    