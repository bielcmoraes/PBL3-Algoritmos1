#Importa bibliotecas
import os
import json
from datetime import date

#Importa funções em outros arquivos
from arquivo_funcoes import *


def inclusaoCliente():

    cliente = {} #Dicionário que armazena as informações referentes ao cliente

    codigo = codigoCliente() #Código de identificação do cliente

    nome = input('Nome do cliente: ').title() #Nome do cliente
    endereco = input('Endereço do cliente: ') #Endereço do cliente
    
    while True:
        try:
            telefone = int(input('Telefone do cliente: '))

        except (TypeError, ValueError):
            print('Digite somente numeros')
        
        if len(str(telefone)) >= 9:
            break
        else:
            print('Telefone inválido')


    cliente["Nome"] = nome
    cliente["Endereco"] = endereco
    cliente["Telefone"] = telefone

    nome_arquivo = saberPasta() + '\\clientes\\cadastro_clientes.json' #Caminho para a pasta correta

    dados = lerArquivo(nome_arquivo) #Recupera ai informações salvas no arquivo

    dados[codigo] = cliente #Atualiza o dicionario recuperado no arquivo com o novo cliente

    salvarArquivo(nome_arquivo, dados)


def codigoCliente():

    nome_arquivo = saberPasta() + '\\clientes\\cadastro_clientes.json' #Caminho para a pasta correta

    clientes = lerArquivo(nome_arquivo) #dicionário com todos os códigos de identificação dos clientes
    
    codigos_cadastrados = list(clientes.keys()) #Lista com códigos dos clientes cadastrados

    #Verifica a quantidade de clientes cadastrados no dia para gerar um novo código
    quantidade_clientes = len(codigos_cadastrados)

    while str(quantidade_clientes) in codigos_cadastrados: #Garante que não exista códigos repetidos
        quantidade_clientes += 1

    codigo_cliente = str(quantidade_clientes) #Codigo de identificação do cliente

    return codigo_cliente

def editarClientes():

    #Edita informações do cliente de acordo com o código
    
    nome_arquivo = saberPasta() + '\\clientes\\cadastro_clientes.json' #Caminho para a pasta correta

    dados = lerArquivo(nome_arquivo)

    codigoCliente = input('Informe o código do cliente: ')

    print('Digite [1] para alterar o NOME do cliente.')
    print('Digite [2] para alterar o ENDEREÇO do cliente.')
    print('Digite [3] para alterar o TELEFONE do cliente.')

    escolha = int(input('>>'))

    if escolha == 1:
        print('Digite um novo nome para o cliente.')
        novoNome = input('>>').title()

        dados[codigoCliente]['Nome'] = novoNome
    
    elif escolha == 2:
        print('Digite um novo endereço para o cliente.')
        novoEndereco = input('>>')

        dados[codigoCliente]['Endereco'] = novoEndereco
    
    elif escolha == 3:
        print('Digite um novo telefone para o cliente.')
        
        while True:
            try:
                novoTelefone = input('>>')

            except (TypeError, ValueError):
                print('Digite somente numeros')
            
            if len(str(novoTelefone)) >= 9:
                break
            else:
                print('Telefone inválido')

        dados[codigoCliente]['Telefone'] = novoTelefone

    salvarArquivo(nome_arquivo)

def excluirCliente():

    nome_arquivo = saberPasta() + '\\clientes\\cadastro_clientes.json' #Caminho para a pasta correta

    dados = lerArquivo(nome_arquivo)

    while True:
        try:
            codigoCliente = input('Informe o código do cliente: ')

            nome_cliente = dados[codigoCliente]['Nome']

            print('Digite [1] para EXCLUIR o cliente', nome_cliente)
            print('Ou digite QUALQUER NUMERO para cancelar a exclusão')
            escolha = int(input('>>'))
            if escolha == 1:
                del dados[codigoCliente]
            
            break

        except KeyError:
            print('Digite um código válido.')

    salvarArquivo(nome_arquivo)

def listarCliente():

    dados = lerArquivo('cadastro_clientes.json')

    print('Digite [1] para ver as informações através do código')
    print('Digite [2] para ver todos os clientes cadastrados')

    escolha = int(input('>>'))

    if escolha == 1:

        while True:
            try:
                codigoCliente = input('Informe o código do cliente: ')
                print(dados[codigoCliente])
                break

            except (KeyError):
                print('Digite um código válido.')
    
    elif escolha == 2:

        clientesOrdenados = sorted(dados, key = lambda nome: dados[nome]['Nome']) # Ordena as chaves dos dicionários com base nos nomes do cliente

        for i in clientesOrdenados:
            print(i,dados[i])