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
# Importa bibliotecas
import os
import json
from datetime import date, datetime

#Importa funções em outros arquivos
from arquivo_funcoes import *
from pecas_catalogo import *

def codigoManutencao(codigo_cliente):

    nome_arquivo = saberPasta() + '\\manutencoes\\agenda_manutencao.json' #Caminho para a pasta correta

    manutencao = lerArquivo(nome_arquivo)

    manutencoes_cadastradas = list(manutencao.keys()) #Lista com os códigos de manutenções agendadas

    data_atual = date.today().strftime('%d%m%y') #String da data atual

    contador_diario = 0

    #Conta as manutenções cadastradas no dia com base no código de manutenção
    for i in manutencoes_cadastradas:
        if data_atual in i:
            contador_diario += 1

    
    codigo_manutencao = data_atual + codigo_cliente +'-'+ str(contador_diario) #codigo da manutenção

    while codigoManutencao in manutencoes_cadastradas:
        contador_diario += 1
        codigo_manutencao = data_atual + codigo_cliente +'-'+ str(contador_diario) #codigo da manutenção atualizado

    return codigo_manutencao

def agendarManutencao():

    manutencoes = {}
    
    nome_arquivo_manutencao = saberPasta() + '\\manutencoes\\agenda_manutencao.json' #Caminho para a pasta de manutenções
    nome_arquivo_clientes = saberPasta() + '\\clientes\\cadastro_clientes.json'

    manutencao_agendada = lerArquivo(nome_arquivo_manutencao)

    clientes = lerArquivo(nome_arquivo_clientes)

    codigo_cliente = input('Digite o código do cliente que deseja agendar a manutenção: ')

    while codigo_cliente not in clientes.keys():
        os.system('cls') #Limpa o terminal
        print('Código inválido')
        codigo_cliente = input('Digite o código do cliente que deseja agendar a manutenção: ')
    
    else:
        os.system('cls') #Limpa o terminal
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

    print('Digite a data da manutenção (dd/mm/aa)')
    while True:

        data_manutencao = str(input('>>'))
        
        if len(data_manutencao) == 8 and data_manutencao[2] == '/' and data_manutencao[5] =='/' and data_manutencao[:2].isdigit() and data_manutencao[3:5].isdigit and data_manutencao[6:].isdigit():
            break

        else:
            os.system('cls') #Limpa o terminal
            print('Formato de data inválido')
            print('Digite a data da manutenção (dd/mm/aa)')
    
    print('Digite [1] para ativar a manutenção automática')
    print('Digite [0] para continuar')
    escolha = int(input('>>'))

    #Associa as informações coletadas as respectivas chaves

    manutencoes['Data'] = data_manutencao
    manutencoes['Cliente'] = codigo_cliente
    manutencoes['Nome_da_Peca'] = peca_escolhida[0]
    manutencoes['Validade_da_Peca'] = validade
    manutencoes['Preço'] = preco

    if escolha == 0:
        manutencao_agendada[str(codigoManutencao(codigo_cliente)) + 'M'] = manutencoes #Adiciona a manutenção ao dicionário
    
    elif escolha == 1:
        manutencao_agendada[str(codigoManutencao(codigo_cliente)) + 'A'] = manutencoes #Adiciona a manutenção ao dicionário
    
    salvarArquivo(nome_arquivo_manutencao, manutencao_agendada) #Salva a manutenção agendada na pasta correta

def editarManutencao():
    
    #Edita informações da manutenção de acordo com o código
    nome_arquivo_manutencao = saberPasta() + '\\manutencoes\\agenda_manutencao.json'
    
    dados = lerArquivo(nome_arquivo_manutencao)

    codigo_manutencao = str(input('Informe o código da manutenção: '))

    #Garante que o código seja válido
    while codigo_manutencao not in dados:
        print('Código inválido. Tente outro.')
        codigo_manutencao = input('Informe o código da manutenção: ')
    
    
    print('Digite [1] para alterar a DATA da manutenção.')
    print('Digite [2] para alterar o CLIENTE vinculado à manutenção.')
    print('Digite [3] para alterar a PEÇA da manutenção.')

    escolha = int(input('>>'))

    if escolha == 1:
        print('Digite uma nova data para a manutenção: ')
        while True:

            nova_data = str(input('>>'))
            
            if nova_data[2] == '/' and nova_data[5] =='/' and nova_data[:2].isdigit() and nova_data[3:5].isdigit and nova_data[6:].isdigit():
                break

            else:
                print('Formato de data inválido')

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

        catalogo = catalogo_pecas() #Peças cadastradas no arquivo de catálogo
    
        peca_escolhida = catalogo[nova_peca - 1] #Peça escolhida pelo cliente

        preco = peca_escolhida[1][0] #Preço da peça escolhida

        validade = peca_escolhida[1][1] #Validade da peça escolhida

        dados[codigo_manutencao]['Nome_da_Peca'] = peca_escolhida[0] #Altera o nome da peça
        dados[codigo_manutencao]['Validade_da_Peca'] = validade #Altera a validade com base na nova peça
        dados[codigo_manutencao]['Preço'] = preco #Altera o preço com base na nova peça
    
    salvarArquivo(nome_arquivo_manutencao, dados) #Salva a informação atualizada no arquivo

def excluirManutencao():
    nome_arquivo_manutencao = saberPasta() + '\\manutencoes\\agenda_manutencao.json'

    dados = lerArquivo(nome_arquivo_manutencao)

    while True:
        try:
            codigo_manutencao = input('Informe o código da manutenção: ')

            print('Digite [1] para EXCLUIR a manutenção', codigo_manutencao)
            print('Ou digite QUALQUER NUMERO para cancelar a exclusão')
            escolha = int(input('>>'))
            if escolha == 1:
                del dados[codigo_manutencao]
            
            break
            
        except KeyError:
            print('Digite um código válido.')
    
    salvarArquivo(nome_arquivo_manutencao, dados) #Salva a informação atualizada no arquivo


def realizarManutencao():
    
    #Variaveis referentes as manutenções agedadas
    nome_arquivo_manutencao_agendada = saberPasta() + '\\manutencoes\\agenda_manutencao.json'
    dados = lerArquivo(nome_arquivo_manutencao_agendada)

    #Variaveis referentes as manutenções realizadas
    nome_arquivo_manutencao_realizada = saberPasta() + '\\manutencoes\\realizada_manutencao.json'
    realizadas = lerArquivo(nome_arquivo_manutencao_realizada)

    while True:
        try:
            codigo_manutencao = input('Informe o código da manutenção: ')
            manutencao_agendada = dados[codigo_manutencao]
            break
            
        except KeyError:
            print('Digite um código válido.')

    realizadas[codigo_manutencao] = dados[codigo_manutencao]

    data_atual = date.today().strftime('%d/%m/%y') #String da data atual
    
    realizadas[codigo_manutencao]['DataR'] = data_atual 

    #Agenda a mautenção automática
    if codigo_manutencao[-1] == 'A':
        automatica = {}

        automatica['Data'] = somarData(data_atual, dados[codigo_manutencao]['Validade_da_Peca']) #Soma a validade da peça com a data que a ultima manutenção foi realizada
        automatica['Cliente'] = dados[codigo_manutencao]['Cliente']
        automatica['Nome_da_Peca'] = dados[codigo_manutencao]['Nome_da_Peca']
        automatica['Validade_da_Peca'] = dados[codigo_manutencao]['Validade_da_Peca']
        automatica['Preço'] = dados[codigo_manutencao]['Preço']
        
        dados[codigoManutencao(dados[codigo_manutencao]['Cliente']) + 'A'] = automatica #Adiciona a manutenção a lista de agendadas com um código novo
    
    del dados[codigo_manutencao]

    salvarArquivo(nome_arquivo_manutencao_agendada, dados) #Salva as manutenções agendadas
    salvarArquivo(nome_arquivo_manutencao_realizada, realizadas)

def listarManutencoes():
    print('Digite [1] para visualizar as MANUTENÇÕES AGENDADAS')
    print('Digite [2] para visualizar as MANUTENÇÕES REALIZADAS\n')
    
    escolha = int(input('>>'))

    if escolha == 1:

        os.system('cls') #Limpa a tela

        #Lista as manutenções agendadas organizadas por data.

        nome_arquivo_manutencao_agendada = saberPasta() + '\\manutencoes\\agenda_manutencao.json'
        agendadas = lerArquivo(nome_arquivo_manutencao_agendada)

        agendadas_ordenadas = sorted(agendadas, key = lambda data: datetime.strptime(agendadas[data]['Data'],'%d/%m/%y').date()) #Ordena as chaves dos dicionários com base nos nomes do cliente

        if not agendadas_ordenadas:
            print('Não existe manutenções agendadas')

            input('\n\n\nPressione qualquer tecla para continuar.')
            os.system('cls') #Limpa a tela
        
        else:
            for i in agendadas_ordenadas:
                print(i, agendadas[i])
        
            input('\n\n\nPressione qualquer tecla para continuar.')
            os.system('cls') #Limpa a tela  
    
    elif escolha == 2:

        os.system('cls') #Limpa a tela

        #Lista as manutenções realizadas organizadas por data

        nome_arquivo_manutencao_realizada = saberPasta() + '\\manutencoes\\realizada_manutencao.json'
        realizadas = lerArquivo(nome_arquivo_manutencao_realizada)

        realizadas_ordenadas = sorted(realizadas, key = lambda data: datetime.strptime(realizadas[data]['DataR'],'%d/%m/%y').date()) #Ordena as chaves dos dicionários com base nos nomes do cliente

        if not realizadas_ordenadas:
            print('Não existe manutenções realizadas')

            input('\n\n\nPressione qualquer tecla para continuar.')
            os.system('cls') #Limpa a tela
        
        else:
            for i in realizadas_ordenadas:
                print(i, realizadas[i])
            
            input('\n\n\nPressione qualquer tecla para continuar.')
            os.system('cls') #Limpa a tela

def imprimirManutencoes():

    #Lista as manutenções agendadas organizadas por data.

    nome_arquivo_manutencao_agendada = saberPasta() + '\\manutencoes\\agenda_manutencao.json'
    agendadas = lerArquivo(nome_arquivo_manutencao_agendada)

    agendadas_ordenadas = sorted(agendadas, key = lambda data: datetime.strptime(agendadas[data]['Data'],'%d/%m/%y').date()) # Ordena as chaves dos dicionários com base na data

    with open('lista_manutencoes.txt', 'w', encoding= 'utf8') as arq:
        for i in agendadas_ordenadas:
            arq.write(i + str(agendadas[i]).replace('{', '|').replace('}', '').replace(',', '|') + '\n')
    
    print('Um arquivo com a lista de manutenções agendadas foi gerado.')

    input('\n\n\nPressione qualquer tecla para continuar.')
    os.system('cls') #Limpa a tela

