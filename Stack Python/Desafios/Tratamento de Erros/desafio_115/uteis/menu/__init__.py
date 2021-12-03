def linha():
    print("-"*20)

def cabecalho(msg):
    linha()
    print(msg.center(20))
    linha()

def leiaInt():
    while True:
        try:
            num1 = int(input("Opção: "))
        except (ValueError, TypeError):
            print("ERRO! Tipos de dados inválidos... ")
        except (KeyboardInterrupt):
            print("ERRO. Execução encerrada...")
        else:
            return num1

def menuOpcao(lista):
    i = 1
    cabecalho("MENU PRINCIPAL")
    for l in lista:
        print(f"{i} - {l}")
        i += 1
    linha()
    opcao = leiaInt()
    return opcao
