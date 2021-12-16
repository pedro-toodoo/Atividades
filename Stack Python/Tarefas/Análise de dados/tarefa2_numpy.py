import numpy as np
import random

np.random.seed(5)
array = np.random.randn(10)
print(f"Nº 1:\nArray de float: {array}")

novo_array = array*100
print(f"Array multiplicado por 100: {novo_array}")

array_int = []
for i in novo_array:
    array_int.append(int(i))
print(f"Array de números inteiros: {array_int}")

np.random.seed(10)
print(f"Nº 2: \nMatriz 4x4 preenchida de forma aleatória:")
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
soma_linha = [0, 0, 0, 0]
soma_coluna = [0, 0, 0, 0]
lista = []
for i in range(4):
    for j in range(4):
        matriz[i][j] = np.random.randint(1, 50)
        lista.append(matriz[i][j])
        print(f"{matriz[i][j]:^3}", end=" ")

        #linhas
        if i == 0:
            soma_linha[0] += matriz[0][j]
        elif i == 1:
            soma_linha[1] += matriz[1][j]
        elif i == 2:
            soma_linha[2] += matriz[2][j]
        elif i == 3:
            soma_linha[3] += matriz[3][j]
        #colunas
        if j == 0:
            soma_coluna[0] += matriz[i][0]
        elif j == 1:
            soma_coluna[1] += matriz[i][1]
        elif j == 2:
            soma_coluna[2] += matriz[i][2]
        elif j == 3:
            soma_coluna[3] += matriz[i][3]
    print()

print(f"\nNº 3:\nMédia das linhas:")
maiorl = menorl = 0
posl_menor = posl_maior = 0
for i in range(4):
    print(f"Linha {i+1} = {soma_linha[i]/4}")
    if i == 0:
        maiorl = menorl = soma_linha[i]
        posl_menor = posl_maior = 0
    else:
        if soma_linha[i] > maiorl:
            maiorl = soma_linha[i]
            posl_maior = i
        if soma_linha[i] < menorl:
            menorl = soma_linha[i]
            posl_menor = i
print(f"Maior valor: {maiorl/4} / Posição: {posl_maior}")
print(f"Menor valor: {menorl/4} / Posição: {posl_menor}")

print(f"\nMédia das colunas:")
maiorc = menorc = 0
posc_menor = posc_maior = 0
for i in range(4):
    print(f"Coluna {i+1} = {soma_coluna[i]/4}")
    if i == 0:
        maiorc = menorc = soma_coluna[i]
        posc_menor = posc_maior = 0
    else:
        if soma_coluna[i] > maiorc:
            maiorc = soma_coluna[i]
            posc_maior = i
        if soma_coluna[i] < menorc:
            menorc = soma_coluna[i]
            posc_menor = i
print(f"Maior valor: {maiorc/4} / Posição: {posc_maior}")
print(f"Menor valor: {menorc/4} / Posição: {posc_menor}")


print(f"\nNº 4:")
teste = [1,2,3,4,5,6]
print(teste.count(1))
for i in range(4):
    for j in range(4):
        print(f"{matriz[i][j]} = {lista.count(matriz[i][j])}")
