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
            #Cria o arquivo caso nãos eja encontrado
            with open(nome_arquivo, 'w+', encoding= 'utf8') as arquivo:
                arquivo.write('{}')

def salvarArquivo(nome_arquivo, informacao):
    with open(nome_arquivo, 'w', encoding='utf8') as arq: 
            json.dump(informacao, arq, ensure_ascii= False) #Salva o dicionario atualizado no arquivo

def saberPasta():
    pasta_atual = os.getcwd()
    os.system('cls')
    
    return pasta_atual
