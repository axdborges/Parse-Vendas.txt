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
    debito = "debito entrada"
    boleto = ("boleto saida")
    financiamento = "financiamento saida"
    credito = "credito entrada"
    emprestimo = "recebimento emprestimo entrada"
    vendas = "vendas entrada"
    ted = "recebimento ted entrada"
    doc = "recebimento doc entrada"
    aluguel = "aluguel saida"


class ParsedModel(models.Model):
    tipo = models.CharField(max_length=255, choices=typeOperation.choices, default="asda")
    data = models.DateField()
    valor = models.IntegerField()
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.TimeField()
    dono = models.CharField(max_length=14)
    loja = models.CharField(max_length=19)