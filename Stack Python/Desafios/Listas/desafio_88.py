from random import randint
from time import sleep
jogo = []
aux = []

qnt = int(input("Quantos jogos você quer que sejam sorteados? "))

for j in range(1, qnt+1):
    for i in range(0, 6):
        valor = randint(1, 60)
        if valor not in jogo:
            aux.append(valor)
    jogo.append(aux[:])
    aux.clear()

for i, j in enumerate(jogo):
    print(f"Jogo {i+1}: {j}")
    sleep(1)