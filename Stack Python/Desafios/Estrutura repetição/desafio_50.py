soma = 0
for i in range(0, 6):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        soma = soma + num
print(f"A soma dos valores pares digitados é: {soma}")