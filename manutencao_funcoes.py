import json
from datetime import date
from cliente import lerArquivo
from pecas_catalogo import *

def codigoManutencao(codigo_cliente):
    contadorManutencao = 0

    data_atual = date.today().strftime('%d%m%y') #String da data atual

    codigo_manutencao = data_atual + codigo_cliente #codigo da manutenção

    return codigo_manutencao

def agendarManutencaoManual():
    
    manutencao_agendada = {}

    clientes = lerArquivo('clientes_arq.json')

    codigo_cliente = input('Digite o código do cliente que deseja agendar a manutenção: ')

    if codigo_cliente in clientes.keys():
        print('Escolha a peça que deseja realizar manutenção\n')

        print('Digite [1] para Filtro de Polipropileno')
        print('Digite [2] para Cartucho Carvão PHB')
        print('Digite [3] para Bucha Difusora Completa')
        print('Digite [4] para Bica móvel')
        print('Digite [5] para Mangueira branca para purificador de água')
        print('Digite [6] para Adaptador Conexão com Rosca')
        print('Digite [7] para Cabeçote de Limpeza')
        print('Digite [8] para Contágua Europa\n')

    
    peca = int(input('>>'))
    catalogo = catalogo_pecas() #Peças cadastradas no arquivo main
    
    peca_escolhida = catalogo[peca - 1] #Peça escolhida pelo cliente

    preco = peca_escolhida[1][0] #Preço da peça escolhida

    validade = peca_escolhida[1][1] #Validade da peça escolhida

    print('Digite a data da manutenção')
    while True:

        data_manutencao = input('>>')
        
        if 5 > len(str(data_manutencao)) < 8 and data_manutencao.isdigit() == True:
            break

        else:
            print('Formato de data inválido')
    
    manutencao_agendada['Data'] = data_manutencao
    manutencao_agendada['Cliente'] = codigo_cliente
    manutencao_agendada['Nome_da_Peca'] = peca_escolhida[0]
    manutencao_agendada['Validade_da_Peca'] = validade
    manutencao_agendada['Preço'] = preco

    dados = lerArquivo('manutencoes_agen_arq.json') #Atualiza o dicionário com os dados já cadastrados
    dados[str(codigoManutencao(codigo_cliente))] = manutencao_agendada

    with open('manutencoes_agen_arq.json', 'w') as arq: 
        json.dump(dados, arq) #Salva o dicionario atualizado no arquivo


def editarManutencao():
    
    #Edita informações da manutenção de acordo com o código

    dados = lerArquivo('manutencoes_agen_arq.json')

    codigo_manutencao = input('Informe o código da manutenção: ')

    print('Digite [1] para alterar a DATA da manutenção.')
    print('Digite [2] para alterar o CLIENTE vinculado à manutenção.')
    print('Digite [3] para alterar a PEÇA da manutenção.')

    escolha = int(input('>>'))

    if escolha == 1:
        nova_data = input('Digite uma nova data para a manutenção: ')

        dados[codigo_manutencao]['Data'] = nova_data
    
    elif escolha == 2:
        novo_cliente = input('Digite o código do novo cliente: ')

        dados[codigo_manutencao]['Cliente'] = novo_cliente
    
    elif escolha == 3:
        print('Escolha a nova peça que deseja realizar manutenção\n')

        print('Digite [1] para Filtro de Polipropileno')
        print('Digite [2] para Cartucho Carvão PHB')
        print('Digite [3] para Bucha Difusora Completa')
        print('Digite [4] para Bica móvel')
        print('Digite [5] para Mangueira branca para purificador de água')
        print('Digite [6] para Adaptador Conexão com Rosca')
        print('Digite [7] para Cabeçote de Limpeza')
        print('Digite [8] para Contágua Europa\n')

        nova_peca = int(input('>>'))

        catalogo = catalogo_pecas() #Peças cadastradas no arquivo main
    
        peca_escolhida = catalogo[nova_peca - 1] #Peça escolhida pelo cliente

        preco = peca_escolhida[1][0] #Preço da peça escolhida

        validade = peca_escolhida[1][1] #Validade da peça escolhida

        dados[codigo_manutencao]['Nome_da_Peca'] = peca_escolhida[0] #Altera o nome da peça
        dados[codigo_manutencao]['Validade_da_Peca'] = validade #Altera a validade com base na nova peça
        dados[codigo_manutencao]['Preço'] = preco #Altera o preço com base na nova peça
    
    with open('manutencoes_agen_arq.json', 'w') as arq: 
        json.dump(dados, arq) #Salva o dicionario atualizado no arquivo

def excluirManutencao():

    dados = lerArquivo('manutencoes_agen_arq.json')

    while True:
        try:
            codigo_manutencao = input('Informe o código da manutenção: ')
            del dados[codigo_manutencao]
            break
            
        except KeyError:
            print('Digite um código válido.')


def realizarManutencao():
    

    dados = lerArquivo('manutencoes_agen_arq.json')
    realizadas = lerArquivo('manutencoes_reali_arq.json')


    while True:
        try:
            codigo_manutencao = input('Informe o código da manutenção: ')
            manutencao_agendada = dados[codigo_manutencao]
            break
            
        except KeyError:
            print('Digite um código válido.')

    realizadas[codigo_manutencao] = dados[codigo_manutencao]

    del dados[codigo_manutencao]
    
    with open('manutencoes_reali_arq.json', 'w') as arq: 
        json.dump(realizadas, arq) #Salva a no arquivo de manutenções realizadas
    
    with open('manutencoes_reali_arq.json', 'w') as arq: 
        json.dump(manutencao_agendada, arq) #Salva a no arquivo de manutenções agendadas

#agendarManutencaoManual()
#editarManutencao()
#excluirManutencao()
#realizarManutencao()