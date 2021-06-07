'''
******************************************************************************************
Autor: Gabriel Cordeiro Moraes
Componente Curricular: EXA854 - MI - Algoritmos
Concluido em: 31/05/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************
'''
#Importa bibliotecas
import os
import json
from datetime import date

#Importa funções em outros arquivos
from arquivo_funcoes import *

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

def editarClientes():

    #Edita informações do cliente de acordo com o código
    
    nome_arquivo = saberPasta() + '\\clientes\\cadastro_clientes.json' #Caminho para a pasta correta

    dados = lerArquivo(nome_arquivo)

    while True:
        try:
            codigoCliente = input('Informe o código do cliente: ')
            testar_código = dados[codigoCliente]
            break
        
        except KeyError:

            os.system('cls')
            print('Código inválido')

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

    salvarArquivo(nome_arquivo,dados)

def excluirCliente():

    nome_arquivo_cliente = saberPasta() + '\\clientes\\cadastro_clientes.json' #Caminho para a pasta clintes
    nome_arquivo_manutencao = saberPasta() + '\\manutencoes\\agenda_manutencao.json' #Caminho para a pasta manutencao

    dados = lerArquivo(nome_arquivo_cliente)

    while True:
        try:
            codigoCliente = input('Informe o código do cliente: ') #Código do Cluiente a ser excluido 

            nome_cliente = dados[codigoCliente]['Nome']

            #Verifica se o usuario quer realmente excluir o cliente informado 
            print('Digite [1] para EXCLUIR o cliente', nome_cliente)
            print('Ou digite QUALQUER NUMERO para cancelar a exclusão')
            escolha = int(input('>>'))

            if escolha == 1:

                # Verifica o código informado está vinculado a uma manutenção
                manutencao_agendada = lerArquivo(nome_arquivo_manutencao)

                for i in manutencao_agendada:
                    if codigoCliente not in manutencao_agendada[i]['Cliente']:
                        del dados[codigoCliente] #Remove o cliente do dicionário
                    else:
                        print('Não é possivel excluir clientes com manutenções agendadas')
                
            break

        except KeyError:
            print('Digite um código válido.')

    salvarArquivo(nome_arquivo_cliente,dados)

def listarCliente():
    nome_arquivo_cliente = saberPasta() + '\\clientes\\cadastro_clientes.json' #Caminho para a pasta clintes

    dados = lerArquivo(nome_arquivo_cliente)

    print('Digite [1] para ver as informações através do código')
    print('Digite [2] para ver todos os clientes cadastrados')

    escolha = int(input('>>'))

    if escolha == 1:
        
        os.system('cls') #Limpa a tela

        while True:
            try:
                codigoCliente = input('Informe o código do cliente: ')
                print('\n')
                print(dados[codigoCliente])
                print('\n')
                input('Pressione qualquer tecla para continuar.')
                os.system('cls') #Limpa a tela
                break

            except (KeyError):
                os.system('cls')
                print('Digite um código válido.')
    
    elif escolha == 2:

        os.system('cls') #Limpa a tela

        # Ordena as chaves dos dicionários com base nos nomes do cliente
        clientesOrdenados = sorted(dados, key = lambda nome: dados[nome]['Nome'])

        #Printa a lista ordenada elemento a elemento 
        for i in clientesOrdenados:
            print(i,dados[i])
        
        input('\n\n\nPressione qualquer tecla para continuar.')
        os.system('cls') #Limpa a tela