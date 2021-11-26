num = 0
soma = 0
while num != 999:
    num = int(input("Digite um número: "))
    if num != 999:
        soma += num
print(f"Somatório dos números: {soma}")