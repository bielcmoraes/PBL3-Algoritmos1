import os
import keyboard
from time import sleep

from artes import *


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

    titulo = titulo_programa()
    print(titulo)

    for linha in tela_menu:
        print(''.join(linha))
    
    sleep(0.1)
    os.system('cls')

def controlarMenu(opcao_menu):
    opcao_escolhida = 55

    if keyboard.is_pressed('down'): #Movimento de seleção do menu
        opcao_menu += 1

        if opcao_menu > 3:
            opcao_menu = 0
    
    if keyboard.is_pressed('Up'): #Movimento de seleção do menu
        opcao_menu -= 1

        if opcao_menu < 0:
            opcao_menu = 3
    
    if keyboard.is_pressed('enter') and opcao_menu == 0: #Acessa as opções relacionadas aos clientes
        opcao_escolhida = opcao_menu
    
    elif keyboard.is_pressed('enter') and opcao_menu == 1: #Acessa as opções relacionadas a manutenção
        opcao_escolhida = opcao_menu
    
    elif keyboard.is_pressed('enter') and opcao_menu == 2: #Acessa o balanço do mês
        opcao_escolhida = opcao_menu
    
    elif keyboard.is_pressed('enter') and opcao_menu == 3: #Finaliza o programa
        exit()
    
    return opcao_menu, opcao_escolhida

def controlarSubMenu(opcao_menu):
    if keyboard.is_pressed('down'): #Movimento de seleção do menu
        opcao_menu += 1

        if opcao_menu > 5:
            opcao_menu = 0
    
    if keyboard.is_pressed('Up'): #Movimento de seleção do menu
        opcao_menu -= 1

        if opcao_menu < 0:
            opcao_menu = 3
    
    return opcao_menu


def subMenu(opcao_menu, opcao_escolhida):

    tela_menu = []
    vazio = str(' ')
    for i in range(6):
        linha = []
        for j in range(3):
            linha.append(vazio)
        
        tela_menu.append(linha)

    if opcao_escolhida == 0:

        tela_menu[0][1] = 'ADICIONAR CLIENTES'
        tela_menu[1][1] = 'EDITAR DADOS DOS CLIENTES'
        tela_menu[2][1] = 'EXCLUIR CLIENTE'
        tela_menu[3][1] = 'LISTAR CLIENTES'
        tela_menu[opcao_menu][0] = '>'
        tela_menu[opcao_menu][2] = '<'

        titulo = texto()
        print(titulo)

        for linha in tela_menu:
            print(''.join(linha))
        
        sleep(0.1)
        os.system('cls')
        return opcao_menu
    
    elif opcao_escolhida == 1:

        tela_menu[0][1] = 'AGENDAR MANUTENÇÃO'
        tela_menu[1][1] = 'EDITAR MANUTENÇÃO'
        tela_menu[2][1] = 'EXCLUIR MANUTENÇÃO'
        tela_menu[3][1] = 'REALIZAR MANUTENÇÃO'
        tela_menu[4][1] = 'LISTAR MANUTENÇÕES'
        tela_menu[5][1] = 'IMPRIMIR MANUTENÇÕES'
        tela_menu[opcao_menu][0] = '>'
        tela_menu[opcao_menu][2] = '<'

        titulo = texto()
        print(titulo)

        for linha in tela_menu:
            print(''.join(linha))
        
        sleep(0.1)
        os.system('cls')
        return opcao_menu

def mainMenu(contador):
    (contador, opcao_escolhida) = controlarMenu(contador)
    menuPrincipal(contador)
    
    if 0 <= opcao_escolhida <= 3:
        return contador, opcao_escolhida

    return contador, None

def mainSubMenu(contador, opcao_escolhida):
    contador = controlarSubMenu(contador)
    opcaoSubMenu = subMenu(contador, opcao_escolhida)
    return contador, opcaoSubMenu

def central_de_controle():
    contador = 0
    contadorSubMenu = 0
    while True: #Executa a tela de menu
        (contador, opcaoSubMenu) = mainMenu(contador)
        
        if opcaoSubMenu != None:
            while True: #Executa a tela de submenu
                (contadorSubMenu, opcaoFinal) = mainSubMenu(contadorSubMenu, opcaoSubMenu)
                
                if keyboard.is_pressed('esc'): #Retorna ao menu principal
                    break
                
                elif keyboard.is_pressed('enter'):
                    if opcaoSubMenu == 0: #Acessa as opções relacionadas aos clientes

                        if contadorSubMenu == 0:
                            print("AQUI ENTRA A FUNÇÃO DE ADICIONAR CLIENTE")
                            sleep(3)
                            break
                        
                        elif contadorSubMenu == 1:
                            print("AQUI ENTRA A FUNÇÃO DE EDITAR CLIENTE")
                            sleep(3)
                            break
                        
                        elif contadorSubMenu == 2:
                            print('AQUI EXCLUI CLIENTE')
                            sleep(3)
                            break

                        elif contadorSubMenu == 3:
                            print("AQUI LISTA OS CLIENTES")
                            sleep(3)
                            break
                    
                    if opcaoSubMenu == 1: #Acessa opções relacionadas a manutenção

                        if contadorSubMenu == 0:
                            print("AQUI ENTRA A FUNÇÃO DE AGENDAR MANUTENÇÃO")
                            sleep(3)
                            break

                        elif contadorSubMenu == 1:
                            print("AQUI ENTRA A FUNÇÃO DE EDITAR MANUTENÇÃO")
                            sleep(3)
                            break

                        elif contadorSubMenu == 2:
                            print("AQUI ENTRA A FUNÇÃO DE EXCLUIR MANUTENÇÃO")
                            sleep(3)
                            break

                        elif contadorSubMenu == 3:
                            print("AQUI ENTRA A FUNÇÃO DE REALIZAR MANUTENÇÃO")
                            sleep(3)
                            break

                        elif contadorSubMenu == 4:
                            print("AQUI ENTRA A FUNÇÃO DE LISTAR MANUTENÇÕES")
                            sleep(3)
                            break

                        elif contadorSubMenu == 5:
                            print("AQUI ENTRA A FUNÇÃO DE IMPRIMIR MANUTENÇÕES")
                            sleep(3)
                            break


#Programa Principal
while True:
    (primeira_escolha, escolha_final) = central_de_controle()
        
        
        
        
        

    