from django.shortcuts import render, HttpResponse
import pandas as pd
import sqlite3 
from sqlite3 import Error
import ipdb

from .forms import CnabForm
from .serializers import ParseInfoSerializer
from .models import ParsedModel

class ParseCnab():
  parsed_infos = ParsedModel.objects.all()
 
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
          form = CnabForm()
      
      context = {
          'form': form
      }
      return TableCnab.generate_table(ParseCnab.parsed_infos)
  
  def handle_uploaded_file(file: bytes):
    infos = file.readlines()
    
    for info in infos:
      # ipdb.set_trace()
      ParseCnab.handle_line(info.decode("utf8"))

  def handle_line(line: bytes):
    string_line = str(line)
    string_clean = string_line[0:string_line.find("\\n\\r")-1]
    ParseInfoSerializer.createInfoModel(string_clean)


class TableCnab():

  def generate_table(query):

    read_table = pd.read_sql("SELECT * FROM parser_parsedmodel", 
    # "C:\\Users\\axdbo\\OneDrive\\Área de Trabalho\\Kenzie\\m6\\Parse-CNAB_doc\\db.sqlite3")
    sqlite3.connect("C:\\Users\\axdbo\\OneDrive\\Área de Trabalho\\Kenzie\\m6\\Parse-CNAB_doc\\db.sqlite3"))

    table_html = read_table.to_html()
    return HttpResponse(table_html)
    

