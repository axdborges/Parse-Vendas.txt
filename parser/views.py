from django.shortcuts import render, HttpResponse
import pandas as pd
import sqlite3 
from pathlib import Path

from .forms import CnabForm
from .serializers import ParseInfoSerializer
from .models import ParsedModel

BASE_DIR = Path(__file__).resolve().parent.parent

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
      ParseCnab.handle_line(info.decode("utf8"))

  def handle_line(line: bytes):
    string_line = str(line)
    string_clean = string_line[0:string_line.find("\\n\\r")-1]
    ParseInfoSerializer.createInfoModel(string_clean)


class TableCnab():

  def generate_table(query):

    read_table = pd.read_sql("SELECT * FROM parser_parsedmodel", 
    sqlite3.connect(f"{BASE_DIR}/db.sqlite3"))

    read_bar = pd.read_sql("SELECT SUM(valor) AS saldo_bar FROM parser_parsedmodel WHERE loja LIKE 'BA%'", 
    sqlite3.connect(f"{BASE_DIR}/db.sqlite3"))
    
    read_mercearia = pd.read_sql("SELECT SUM(valor) AS saldo_mercearia FROM parser_parsedmodel WHERE loja LIKE 'MERCE%'", 
    sqlite3.connect(f"{BASE_DIR}/db.sqlite3"))
    
    read_loja = pd.read_sql("SELECT SUM(valor) AS saldo_loja FROM parser_parsedmodel WHERE loja LIKE 'LO%'", 
    sqlite3.connect(f"{BASE_DIR}/db.sqlite3"))
    
    read_mercado = pd.read_sql("SELECT SUM(valor) AS saldo_mercado FROM parser_parsedmodel WHERE loja LIKE 'MERCA%'", 
    sqlite3.connect(f"{BASE_DIR}/db.sqlite3"))

    table_html = read_table.to_html()
    saldo_bar = read_bar.to_html()
    saldo_mercearia = read_mercearia.to_html()
    saldo_loja = read_loja.to_html()
    saldo_mercado = read_mercado.to_html()
    response = table_html + saldo_bar + saldo_mercearia + saldo_loja + saldo_mercado
    return HttpResponse(response)
    

