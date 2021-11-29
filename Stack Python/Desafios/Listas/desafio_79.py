lista = []
i = 0
while True:
    num = int(input("Adicione um valor: "))
    if num not in lista:
        lista.append(num)
        print(f"Valor {num} adicionado na lista! ")
    else:
        print("Valor já existente na lista. Não foi adicionado! ")

    opcao = input("Deseja continuar? [S/N]")
    if opcao in 'Nn':
        break

lista.sort()
print(f"Lista criada e ordenada: {lista}")