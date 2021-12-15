import numpy as np

print(f"Nº 1:\nValores igualmente espaçados: {np.linspace(0, 1, 30)}")


arr1 =[]
arr2 = []
for i in range(0, 52):
    if i % 2 == 0:
        arr1.append(i)
for i in range(100, 49, -1):
    if i % 2 == 0:
        arr2.append(i)
print("\nNº 2:")
print(f"Array 1 de 0 até 51: {arr1}")
print(f"Array 2 de 100 até 50: {arr2}")
arr2.sort()
concat = np.concatenate((arr1, arr2), )
print(f"Arrays concatenados e ordenados: {concat}")

print("\nNº 3:")
print(f"Arrays concatenados e ordenados de 0 a 100: {concat}")

print("\nNº 4:")
matriz = np.ones((3, 4))
print(f"Matriz preenchida com um: \n{matriz}")
arr_matriz = []
for i in range(0, 3):
    for j in range(0, 3):
        arr_matriz.append(matriz[i][j])
print(f"Lista criada à partir da matriz 3x4 preenchida por 1: {arr_matriz}")


print("\nNº 5:")
while True:
    try:
        linhas = int(input("Número de linhas: "))
    except:
        print("Valor inválido")
    else:
        break
while True:
    try:
        colunas = int(input("Número de colunas: "))
    except:
        print("Valor inválido")
    else:
        break

tamanho = colunas * linhas
print(f"Matriz {linhas}x{colunas}")
if tamanho % 2 == 0:
    print(f"Tamanho do vetor é par ({tamanho} elementos) ")
else:
    print(f"Tamanho do vetor é ímpar ({tamanho} elementos) ")










