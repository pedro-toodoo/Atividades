num = input("Digite um número de 0 a 9999: ")

aux = " ".join(num)
lista = aux.split()

if len(lista) == 1:
    print(f"Unidade: {lista[0]}")

if len(lista) == 2:
    print(f"Dezena: {lista[0]}")
    print(f"Unidade: {lista[1]}")

if len(lista) == 3:
    print(f"Centena: {lista[0]}")
    print(f"Dezena: {lista[1]}")
    print(f"Unidade: {lista[2]}")

if len(lista) == 4:
    print(f"Milhar: {lista[0]}")
    print(f"Centena: {lista[1]}")
    print(f"Dezena: {lista[2]}")
    print(f"Unidade: {lista[3]}")


