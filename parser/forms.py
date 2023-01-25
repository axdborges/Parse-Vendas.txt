from django import forms
from parser.models import InfoModel

class CnabForm(forms.Form):
    archive = forms.FileField(required=False)
    

    
    

