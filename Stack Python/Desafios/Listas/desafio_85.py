lista = [[], []]
dados = []

for i in range(0, 7):
    num = int(input("Digite um valor: "))

    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

print(f"Lista completa: {lista}")
print(f"Lista de pares: {lista[0]}")
print(f"Lista de ímpares: {lista[1]}")