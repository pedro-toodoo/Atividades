num = float(input("Digite um número: "))

print("Digite 1 para saber se o número é par ou ímpar")
print("Digite 2 para saber se o número é positivo ou negativo")
print("Digite 3 para saber se o número é inteiro ou decimal")
opcao = int(input("Opção: "))

if opcao == 1:
    if num % 2 == 0:
        print(f"{num} é par!")
    else:
        print(f"{num} é ímpar!")

elif opcao == 2:
    if num >= 0:
        print(f"{num} é positivo!")
    else:
        print(f"{num} é negativo!")

elif opcao == 3:
    if float.is_integer(num):
        print(f"{int(num)} é inteiro!")
    else:
        print(f"{num} é decimal!")