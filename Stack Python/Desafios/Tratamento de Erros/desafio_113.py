def leiaInt():
    while True:
        try:
            num1 = int(input("Digite um número inteiro: "))
        except (ValueError, TypeError):
            print("ERRO! Tipos de dados inválidos... ")
        except (KeyboardInterrupt):
            print("ERRO. Execução encerrada...")
        else:
            return num1
def leiaFloat():
    while True:
        try:
            num2 = float(input("Digite um número real: "))
        except (ValueError, TypeError):
            print("ERRO! Tipos de dados inválidos... ")
        except (KeyboardInterrupt):
            print("ERRO. Execução encerrada...")
        else:
            return num2

n1 = leiaInt()
n2 = leiaFloat()
print(f"Valor inteiro: {n1}")
print(f"Valor real: {n2}")