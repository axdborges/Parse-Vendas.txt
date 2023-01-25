from django.urls import path 

from parser.views import ParseCnab

urlpatterns = [
    path('index/', ParseCnab.form_cnab, name='form_cnab')
]