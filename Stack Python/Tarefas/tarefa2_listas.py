from random import randint
from time import sleep

dado = []
aux = []
cont1 = cont2 = cont3 = cont4 = cont5 = cont6 = 0

for j in range(1, 101):
    valor = randint(1, 6)
    aux.append(valor)
    dado.append(aux[:])
    aux.clear()
    if valor == 1:
        cont1 += 1
    elif valor == 2:
        cont2 += 1
    elif valor == 3:
        cont3 += 1
    elif valor == 4:
        cont4 += 1
    elif valor == 5:
        cont5 += 1
    elif valor == 6:
        cont6 += 1

for i, d in enumerate(dado):
    print(f"Jogada {i+1}: {d}")

print(f"Quantidade de vezes que caiu número 1: {cont1}")
print(f"Quantidade de vezes que caiu número 2: {cont2}")
print(f"Quantidade de vezes que caiu número 3: {cont3}")
print(f"Quantidade de vezes que caiu número 4: {cont4}")
print(f"Quantidade de vezes que caiu número 5: {cont5}")
print(f"Quantidade de vezes que caiu número 6: {cont6}")