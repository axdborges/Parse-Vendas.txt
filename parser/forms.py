from django import forms

class CnabForm(forms.Form):
    Archive: forms.FileField(label="Arquivo")
    