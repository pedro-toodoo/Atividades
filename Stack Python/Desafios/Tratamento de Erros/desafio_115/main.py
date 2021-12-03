from uteis.menu import *

while True:
    resp = menuOpcao(["Cadastrar", "Listar", "Sair"])

    if resp == 1:
        print("Opção 1")
    elif resp == 2:
        print("Opção 2")
    elif resp == 3:
        print("Saindo...")
    else:
        print("Opção inválida")