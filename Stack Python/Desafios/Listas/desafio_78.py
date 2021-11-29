lista = []
maior = 0
menor = 0

for i in range(0, 5):
    lista.append(int(input("Digite um valor: ")))
    if i == 0:
        maior = menor = lista[i]

    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]

print(f"Lista criada: {lista}")
print(f"Maior valor: {maior} / nas posições ", end="")
for pos, valor in enumerate(lista):
    if lista[pos] == maior:
        print(f"{pos}", end=" ")

print(f"\nMenor valor: {menor} / na posições ", end="")
for pos, valor in enumerate(lista):
    if lista[pos] == menor:
        print(f"{pos}", end=" ")