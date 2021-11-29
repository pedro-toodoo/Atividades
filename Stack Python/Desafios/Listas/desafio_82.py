lista = []
lista_par = []
lista_impar = []
i = 0
while True:
    lista.append(int(input("Digite um valor: ")))

    if lista[i] % 2 == 0:
        lista_par.append(lista[i])
    else:
        lista_impar.append(lista[i])

    i += 1

    opcao = input("Deseja continuar [S/N]? ")
    if opcao in 'Nn':
        break

print(f"Lista completa: {lista}")
print(f"Lista de números pares: {lista_par}")
print(f"Lista de números ímpares: {lista_impar}")