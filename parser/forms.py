from django import forms

class CnabForm(forms.Form):
    archive = forms.FileField(required=False)
    

    
    

