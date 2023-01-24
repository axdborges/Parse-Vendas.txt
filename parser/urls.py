from django.urls import path 

from parser import views

urlpatterns = [
    path('index/', views.form_cnab, name='form_cnab')
]