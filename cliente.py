import json
from datetime import date

def inclusaoCliente():

    cliente = {} #Dicionário que armazena as informações referentes ao cliente

    codigo = codigoCliente() #Código de identificação do cliente

    nome = input('Nome do cliente: ').title()
    endereco = input('Endereço do cliente: ')
    
    while True:
        try:
            telefone = int(input('Telefone do cliente: '))

        except (TypeError, ValueError):
            print('Digite somente numeros')
        
        if len(str(telefone)) >= 10:
            break
        else:
            print('Telefone inválido')


    cliente["Nome"] = nome
    cliente["Endereco"] = endereco
    cliente["Telefone"] = telefone

    dados = lerArquivo('clientes.json') #Recupera ai informações salvas no arquivo

    dados[codigo] = cliente #Atualiza o dicionario recuperado no arquivo com o novo cliente

    with open('clientes.json', 'w') as arq: 
        json.dump(dados, arq) #Salva o dicionario atualizado no arquivo

def codigoCliente():
    contador_clientes = 0

    clientes = lerArquivo('clientes.json') #Lista com todos os códigos de identificação dos clientes
    
    #Verifica a quantidade de clientes cadastrados no dia para gerar um novo código
    for i in clientes:
        contador_clientes += 1
    
    codigo_cliente = str(contador_clientes) #Codigo de identificação do cliente

    return codigo_cliente


def lerArquivo (nome_arquivo):

    #Ler o arquivos no formato .Json e retorna os dados convertidos nas respectivas estruturas de dados
    with open(nome_arquivo, 'r') as arquivo:
        dados_lidos = json.load(arquivo)
        return dados_lidos

def editarClientes():

    #Edita informações do cliente de acordo com o código
    
    dados = lerArquivo('clientes.json')

    codigoCliente = input('Informe o código do cliente: ')

    print('Digite [1] para alterar o NOME do cliente.')
    print('Digite [2] para alterar o ENDEREÇO do cliente.')
    print('Digite [1] para alterar o TELEFONE do cliente.')

    escolha = int(input('>>'))

    if escolha == 1:
        print('Digite um novo nome para o cliente.')
        novoNome = input('>>').title()

        dados[codigoCliente]['Nome'] = novoNome

        with open('clientes.json', 'w') as arq: 
            json.dump(dados, arq) #Salva o dicionario atualizado no arquivo
    
    elif escolha == 2:
        print('Digite um novo endereço para o cliente.')
        novoEndereco = input('>>')

        dados[codigoCliente]['Endereco'] = novoEndereco

        with open('clientes.json', 'w') as arq: 
            json.dump(dados, arq) #Salva o dicionario atualizado no arquivo
    
    elif escolha == 3:
        print('Digite um novo telefone para o cliente.')
        
        while True:
            try:
                novoTelefone = input('>>')

            except (TypeError, ValueError):
                print('Digite somente numeros')
            
            if len(str(novoTelefone)) >= 10:
                break
            else:
                print('Telefone inválido')

        dados[codigoCliente]['Telefone'] = novoTelefone

        with open('clientes.json', 'w') as arq: 
            json.dump(dados, arq) #Salva o dicionario atualizado no arquivo

def excluirCliente():

    dados = lerArquivo('clientes.json')

    while True:
        try:
            codigoCliente = input('Informe o código do cliente: ')
            del dados[codigoCliente]
            
        except KeyError:
            print('Digite um código válido.')

    with open('clientes.json', 'w') as arq: 
            json.dump(dados, arq) #Salva o dicionario atualizado no arquivo

def listarCliente():

    dados = lerArquivo('clientes.json')

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