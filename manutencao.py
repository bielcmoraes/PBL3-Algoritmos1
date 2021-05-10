import json
from datetime import date

def codigoManutencao(codigo_cliente):
    contadorManutencao = 0

    data_atual = date.today().strftime('%d%m%y') #String da data atual

    codigo_manutencao = data_atual + codigo_cliente