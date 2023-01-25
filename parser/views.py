from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
import ipdb

from .forms import CnabForm
from .serializers import ParseInfoSerializer

class ParseCnab():

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
          ParseCnab.handle_uploaded_file(archive)
          # cnab = form.save()
          form = CnabForm()
      
      context = {
          'form': form
      }
      return render(request, "form.html", context=context)
  
  def handle_uploaded_file(file: bytes):
    # encoding = "utf-8"
    infos = file.readlines()
    for info in infos:
      
      ParseCnab.handle_line(info)
    print()
    return file

  def handle_line(line: bytes):
    string_line = str(line)
    string_clean = string_line[2:string_line.find("\\n\\r")-5]
    ParseInfoSerializer.createInfoModel(string_clean)

    

