import json
from datetime import date
from cliente import lerArquivo
from main import pecas

def codigoManutencao(codigo_cliente):
    contadorManutencao = 0

    data_atual = date.today().strftime('%d%m%y') #String da data atual

    codigo_manutencao = data_atual + codigo_cliente #codigo da manutenção

    return codigo_manutencao

def agendarManutencaoManual():

    clientes = lerArquivo('clientes.json')

    codigo_cliente = input('Digite o código do cliente que deseja agendar a manutenção: ')
    
    for i in clientes.keys():
        if i == codigo_cliente:
            catalogoPecas = pecas()

            for i in catalogoPecas:
                print(i)
            
            break
    
    data_manutencao = input('Digite a data da manutenção: ')
    peca = input('informe a peça a ser trocada: ') 