from django import forms
from parser.models import InfoModel

class CnabForm(forms.Form):
    archive = forms.FileField(required=False)
    # class Meta:
    #     model = InfoModel
    #     fields = "__all__"

    
    

