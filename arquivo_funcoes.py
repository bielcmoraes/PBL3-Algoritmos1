import json
import os
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
    
    return pasta_atual

def balancoMensal():
    print('Informe um MÊS e um ANO')

    while True:
        data = input('>>')
            
        if data[2] == '/' and data[:2].isdigit() and data[3:5].isdigit:
            break

    else:
        print('Formato de data inválido')

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
    print('\n Digite [0] para sair')
    escolha = int(input('>>'))

    if escolha == 1:
        nome_arq_balanco = 'balanco_' + data[:2] + data[3:]
        with open(str(nome_arq_balanco), 'w', encoding= 'utf8') as arq:
            for i in balanco_mes:
                arq.write((str(i) + '\n\n').replace(',','|').replace('{','').replace('}','').replace('[', '').replace(']',''))
            
            arq.write(str('Total mensal: R$ ')+str(total))

        

