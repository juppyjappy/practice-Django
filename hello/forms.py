from django import forms

class IntForm(forms.Form):
    input_num = forms.IntegerField(label='input_num')
    input_p = forms.CharField(label='input_p')