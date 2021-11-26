soma = 0
for i in range(1, 5001):
    if (i % 2 != 0) and (i % 3 == 0):
        soma = soma + i
print(f"Soma dos números entre 1 e 500 múltiplos de 3 e ímpares: {soma}")