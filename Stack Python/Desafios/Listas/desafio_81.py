lista = []
cont = 0

while True:
    lista.append(int(input("Digite um valor: ")))
    cont += 1

    opcao = input("Deseja continuar? [S/N]")
    if opcao in 'Nn':
        break;

print(f"Foram digitados {cont} números! ")
lista.sort(reverse=True)
print(f"Lista em ordem decrescente: {lista}")
if 5 in lista:
    print(f"Sim. O número 5 aparece na lista!")
else:
    print("Não. O número 5 não aparece na lista! ")