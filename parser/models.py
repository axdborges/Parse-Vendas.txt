from django.db import models
 

class InfoModel(models.Model):
    tipo = models.CharField(max_length=1)
    data = models.CharField(max_length=8)
    valor = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.CharField(max_length=6)
    dono = models.CharField(max_length=14)
    loja = models.CharField(max_length=19)
    
class typeOperation(models.Choices):
    debito = "debito"
    boleto = "boleto"
    financiamento = "financiamento"
    credito = "credito"
    emprestimo = "recebimento emprestimo"
    vendas = "vendas"
    ted = "recebimento ted"
    doc = "recebimento doc"
    aluguel = "aluguel"


class ParsedModel(models.Model):
    tipo = models.CharField(max_length=255, choices=typeOperation.choices, default=None)
    natureza = models.CharField(max_length=7, default=None)
    data = models.DateField()
    valor = models.IntegerField()
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.TimeField(auto_now=False, auto_now_add=False)
    dono = models.CharField(max_length=14)
    loja = models.CharField(max_length=19)