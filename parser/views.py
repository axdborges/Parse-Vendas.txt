from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy

from .forms import CnabForm

class IndexView(FormView):
    template_name = 'index.html'
    form_class = CnabForm
    success_url = reverse_lazy('index')

     

