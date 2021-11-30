matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
somacoluna = 0
maior = 0

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input("Digite um valor: "))
        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]
        if j == 2:
            somacoluna += matriz[i][2]
        if i == 1:
            if matriz[1][j] > maior:
                maior = matriz[1][j]

for i in range(0, 3):
    for j in range(0, 3):
        print(matriz[i][j], end="  ")
    print()

print(f"Soma dos valores pares: {soma}")
print(f"Soma dos valores da terceira coluna: {somacoluna}")
print(f"Maior valor da segunda linha: {maior}")