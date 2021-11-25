nome = input("Digite seu nome completo: ")

lista = nome.split()

print(f"Primeiro nome: {lista[0]}")
print(f"Último nome: {lista[len(lista)-1]}")