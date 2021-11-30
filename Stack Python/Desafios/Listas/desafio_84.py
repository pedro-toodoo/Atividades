lista = []
dados = []

cont = 0
maiorPeso = 0
menorPeso = 0

while True:
    dados.append(input("Digite um nome: "))
    dados.append(float(input("Digite o peso: ")))

    if len(lista) == 0:
        maiorPeso = menorPeso = dados[1]
    else:
        if dados[1] > maiorPeso:
            maiorPeso = dados[1]
        if dados[1] < menorPeso:
            menorPeso = dados[1]

    lista.append(dados[:])
    dados.clear()

    opcao = input("Deseja continuar [S/N]? ")
    if opcao in "Nn":
        break

print(f"Lista: {lista}")
print(f"Quantidade de pessoa cadastradas: {len(lista)}")
print(f"Maior peso: {maiorPeso}Kg -> ", end="")

for i in lista:
    if i[1] == maiorPeso:
        print(f"{i[0]}", end=" ")
print(f"\nMenor peso: {menorPeso}Kg -> ", end="")
for i in lista:
    if i[1] == menorPeso:
        print(f"{i[0]}", end=" ")