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

#Importa funções em outros arquivos
from cliente_funcoes import *
from manutencao_funcoes import *
from arquivo_funcoes import *


def menu():
    os.system('cls') #Limpa a tela

    while True:

        print('Digite [1] para acessar os CLIENTES')
        print('Digite [2] para acessar as MANUTENÇÕES')
        print('Digite [3] para acessar o BALANÇO MENSAL')
        print('Digite [0] para ENCERRAR\n')

        escolha = int(input('>>'))

        os.system('cls') #Limpa a tela

        if escolha == 1:
            print('Digite [1] para ADICIONAR clientes')
            print('Digite [2] para EDITAR informações do cliente')
            print('Digite [3] para EXCLUIR cliente')
            print('Digite [4] para LISTAR clientes')
            print('Digite [0] para RETORNAR ao menu principal\n')

            escolha2 = int(input('>>'))

            os.system('cls') #Limpa a tela


            if escolha2 == 1:
                inclusaoCliente()
            
            elif escolha2 == 2:
                editarClientes()
            
            elif escolha2 == 3:
                excluirCliente()
            
            elif escolha2 == 4:
                listarCliente()
            
            elif escolha2 == 0:
                break
        
        elif escolha == 2:
            print('Digite [1] para AGENDAR manutenção')
            print('Digite [2] para EDITAR manutenção')
            print('Digite [3] para EXCLUIR manutenção')
            print('Digite [4] para REALIZAR manutenção')
            print('Digite [5] para LISTAR manutenções')
            print('Digite [6] para IMPRIMIR manutenções agendadas')
            print('Digite [0] para RETORNAR ao menu principal\n')

            escolha2 = int(input('>>'))

            os.system('cls') #Limpa a tela


            if escolha2 == 1:
                agendarManutencao()
            
            elif escolha2 == 2:
                editarManutencao()
            
            elif escolha2 == 3:
                excluirManutencao()
            
            elif escolha2 == 4:
                realizarManutencao()
            
            elif escolha2 == 5:
                listarManutencoes()
            
            elif escolha2 == 6:
                imprimirManutencoes()
            
            elif escolha2 == 0:
                break
        
        elif escolha == 3:
            balancoMensal()
            os.system('cls') #Limpa a tela

        
        elif escolha == 0:
            exit()

while True:
    menu()