from random import randint
from time import sleep
numeros = []

def sortear():
    print(f"Lista com números sorteados: [ ", end="")
    for i in range(0, 5):
        valor = randint(1, 10)
        print(f"{valor}", end=" ")
        sleep(1)
        numeros.append(valor)
    print("]")
#print(len(numeros))

def somaPar(lista):
    soma = 0
    for v in numeros:
        if v % 2 == 0:
            soma += v
    print(f"\nSomatório dos números pares: {soma}")

sortear()
somaPar(numeros)