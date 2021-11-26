num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

print("1 - Somar")
print("2 - Multiplicar")
print("3 - Maior")
print("4 - Novos números")
print("5 - Sair do programa")
opcao = int(input("Opção: "))

while opcao != 5:
    if opcao == 1:
        print(f"Soma de {num1} e {num2}: {num1 + num2}")
    elif opcao == 2:
        print(f"Multiplicação de {num1} e {num2}: {num1*num2}")
    elif opcao == 3:
        if num1 > num2:
            print(f"Maior número: {num1}")
        else:
            print(f"Maior número: {num2}")
    elif opcao == 4:
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite outro número: "))

    opcao = int(input("Opção: "))