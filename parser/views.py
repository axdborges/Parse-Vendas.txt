from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
import ipdb

from .forms import CnabForm

def handle_uploaded_file(file: bytes):
    # encoding = "utf-8"
    infos = file.readlines()
    for info in infos:
        print(info)
    ipdb.set_trace()
    print()
    return file


def form_cnab(request):
    if request.method == "GET":
        form = CnabForm()
        context = {
            "form": form
        }
        return render(request, "form.html", context=context)
    else: 
        form = CnabForm(request.POST, request.FILES)
        if form.is_valid():
            archive = request.FILES.get("archive")
            handle_uploaded_file(archive)
            # cnab = form.save()
            form = CnabForm()
        
        context = {
            'form': form
        }
        return render(request, "form.html", context=context)