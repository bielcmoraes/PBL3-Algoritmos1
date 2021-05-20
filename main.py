def menu():
    print('Digite [1] para acessar os CLIENTES')
    print('Digite [2] para acessar as MANUTENÇÕES')
    print('Digite [3] para acessar o BALANÇO MENSAL')
    print('Digite [0] para ENCERRAR\n')

    escolha = int(input('>>'))

    if escolha == 1:
        print('Digite [1] para ADICIONAR clientes')
        print('Digite [2] para EDITAR informações do cliente')
        print('Digite [3] para EXCLUIR cliente')
        print('Digite [4] para LISTAR clientes')
        print('Digite [0] para RETORNAR ao menu principal\n')

        escolha2 = int(input('>>'))
    
    elif escolha == 2:
        print('Digite [1] para AGENDAR manutenção')
        print('Digite [2] para EDITAR manutenção')
        print('Digite [3] para EXCLUIR manutenção')
        print('Digite [4] para REALIZAR manutenção')
        print('Digite [5] para LISTAR manutenções')
        print('Digite [6] para IMPRIMIR manutenções')
        print('Digite [0] para RETORNAR ao menu principal\n')

        escolha2 = int(input('>>'))
    
    elif escolha == 3:
        print('Digite o MÊS e o ANO do balanço\n')

        data_balanco = input('>>')
    
    elif escolha == 0:
        exit()