import os
import keyboard
from time import sleep

from artes import texto


#Cria a matriz do menu
def menuPrincipal(opcao_menu):
    tela_menu = []
    vazio = str(' ')
    for i in range(4):
        linha = []
        for j in range(3):
            linha.append(vazio)
        
        tela_menu.append(linha)


    tela_menu[0][1] = 'CLIENTES'
    tela_menu[1][1] = 'MANUTENÇÃO'
    tela_menu[2][1] = 'BALANÇO DO MÊS'
    tela_menu[3][1] = 'SAIR'
    tela_menu[opcao_menu][0] = '>'
    tela_menu[opcao_menu][2] = '<'

    titulo = texto()
    print(titulo)

    for linha in tela_menu:
        print(''.join(linha))
    
    sleep(0.1)
    os.system('cls')
    return opcao_menu

def controlarMenu(opcao_menu):

    if keyboard.is_pressed('down'): #Movimento de seleção do menu
        opcao_menu += 1

        if opcao_menu > 3:
            opcao_menu = 0
    
    if keyboard.is_pressed('Up'): #Movimento de seleção do menu
        opcao_menu -= 1

        if opcao_menu < 0:
            opcao_menu = 3
    
    if keyboard.is_pressed('enter') and opcao_menu == 0: #Acessa as opções relacionadas aos clientes
        opcao_cliente = True
    
    if keyboard.is_pressed('enter') and opcao_menu == 1: #Acessa as opções relacionadas a manutenção
        opcao_manutencao = True
    
    if keyboard.is_pressed('enter') and opcao_menu == 2: #Acessa o balanço do mês
        opcao_balancoMensal = True
    
    if keyboard.is_pressed('enter') and opcao_menu == 3: #Finaliza o programa
        exit()