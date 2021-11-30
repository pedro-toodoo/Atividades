lista = [] #tudo
cont = 0

while True:
    nome = input(("Nome do aluno: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))

    media = (nota1 + nota2) / 2

    lista.append([nome, [nota1, nota2], media])
    cont += 1

    opcao = input("Deseja continuar [S/N]? ")
    if opcao in "Nn":
        break

#print(lista)

for i, a in enumerate(lista):
    print(f"Aluno: {a[0]} --> Média: {a[2]}")
    print(f"Notas: {a[1][0]} e {a[1][1]}")
    print("-"*20)