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
import json
import os
from datetime import datetime, timedelta

def lerArquivo(nome_arquivo):
    while True:
        #Ler o arquivos no formato .Json e retorna os dados convertidos nas respectivas estruturas de dados
        try:
            with open(nome_arquivo, 'r', encoding='utf8') as arquivo:
                dados_lidos = json.load(arquivo)
                return dados_lidos
        
        except FileNotFoundError:
            #Cria o arquivo caso nãos seja encontrado
            with open(nome_arquivo, 'w+', encoding= 'utf8') as arquivo:
                arquivo.write('{}')

def salvarArquivo(nome_arquivo, informacao):
    with open(nome_arquivo, 'w', encoding='utf8') as arq: 
            json.dump(informacao, arq, ensure_ascii= False) #Salva o dicionario atualizado no arquivo

def saberPasta():
    pasta_atual = os.getcwd()
    os.system('cls')
    
    return pasta_atual + '\\dados'

def somarData(data_str, meses_somados):
    data = datetime.strptime(data_str,'%d/%m/%y').date() #Converte a data em string para o tipo date

    if meses_somados == None: #Peças com validade indefinida não serão alteradas
        return None
    
    elif meses_somados == 12:
        dias_somados = 365
    
    else:
        dias_somados = meses_somados * 30
    
    data_somada = data + timedelta(days= dias_somados)
    data_somada_str = data_somada.strftime('%d/%m/%y')
    
    return data_somada_str


def balancoMensal():
    print('Informe um MÊS e um ANO (mm/aa)')

    while True:
        data = input('>>')
            
        if len(data) == 5 and data[2] == '/' and data[:2].isdigit() and data[3:5].isdigit:
            break

        else:
            os.system('cls')
            print('Formato de data inválido')
            print('Informe um MÊS e um ANO (mm/aa)')

    nome_arquivo_manutencao_realizada = saberPasta() + '\\manutencoes\\realizada_manutencao.json'
    realizadas = lerArquivo(nome_arquivo_manutencao_realizada)

    total = 0
    balanco_mes = []
    for i in realizadas:
        if realizadas[i]['DataR'][3:] == data:
            balanco_mes.append([i, realizadas[i]])
            total += realizadas[i]['Preço']
    
    for j in balanco_mes:
        print(j)
    
    print('\nO valor total é: ', total)

    print('\nDigite [1] para imprimir o balanço')
    print('\n Digite [0] para retornar ao menu.')
    escolha = int(input('>>'))

    if escolha == 1:
        nome_arq_balanco = saberPasta() + '\\balanco\\balanco_' + data[:2] + data[3:] + '.txt'
        with open(str(nome_arq_balanco), 'w', encoding= 'utf8') as arq:
            for i in balanco_mes:
                arq.write((str(i) + '\n\n').replace(',','|').replace('{','').replace('}','').replace('[', '').replace(']',''))
            
            arq.write(str('Total mensal: R$ ')+str(total))
