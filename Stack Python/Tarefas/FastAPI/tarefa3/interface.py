def linha(qnt):
    print(f"-"*qnt)

def cabecalho(escrita):
    linha(len(escrita))
    print(escrita)
    linha(len(escrita))

def leiaInt():
    while True:
        try:
            opcao = int(input("Opção: "))
        except (ValueError, TypeError):
            print("ERRO! Tipos de dados inválidos... ")
        except (KeyboardInterrupt):
            print("ERRO. Execução encerrada...")
        else:
            return opcao

def menu(lista):
    i = 1
    cabecalho("Cliente Python - API com mongoDB")
    for l in lista:
        print(f"{i} - {l}")
        i += 1
    opcao = leiaInt()
    return opcao

