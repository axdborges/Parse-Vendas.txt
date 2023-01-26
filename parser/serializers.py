from rest_framework import serializers
from .models import  InfoModel, ParsedModel, typeOperation
from datetime import datetime, time


class ParseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoModel
        fields = "__all__"

    def createInfoModel(info: str):
        info_data = {
            "tipo": info[0],
            "data": info[1:9],
            "valor": info[9:19],
            "cpf": info[19:30],
            "cartao": info[30:42],
            "hora": info[42:48],
            "dono": info[48:62],
            "loja": info[62:]
        }
        new_info = InfoModel.objects.create(**info_data)
        ParseInfoSerializer.parseInfos(new_info)
        return new_info

    def parseInfos(info: dict):
        type = ""
        nature = ""
        value = int(info.valor) / 100
        if info.tipo == "1":
            type = typeOperation.debito.value
        elif info.tipo == "2":
            type = typeOperation.boleto.value
        elif info.tipo == "3":
            type = typeOperation.financiamento.value
        elif info.tipo == "4":
            type = typeOperation.credito.value
        elif info.tipo == "5":
            type = typeOperation.emprestimo.value
        elif info.tipo == "6":
            type = typeOperation.vendas.value
        elif info.tipo == "7":
            type = typeOperation.ted.value
        elif info.tipo == "8":
            type = typeOperation.doc.value
        elif info.tipo == "9":
            type = typeOperation.aluguel.value

        if type == "boleto" or type == "financiamento" or type == "aluguel":
            nature = "saida"
            value = -value
        else: 
            nature = "entrada"

        date = datetime.strptime(info.data, '%Y%m%d').date()
        hour = time(int(info.hora[0:2]), int(info.hora[2:4]), int(info.hora[4:6]))
        
        parsed_info_data = {
            "tipo": type,
            "natureza": nature,
            "data": date,
            "valor": value,
            "cpf": info.cpf,
            "cartao": info.cartao,
            "hora": hour,
            "dono": info.dono,
            "loja": info.loja
        }

        new_parsed_info = ParsedModel.objects.create(**parsed_info_data)
        return new_parsed_info

        