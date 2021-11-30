pessoas = {}
lista = []

soma_idade = 0

while True:
    pessoas["nome"] = input("Nome: ")
    pessoas["sexo"] = input("Sexo: ")
    pessoas["idade"] = int(input("Idade: "))

    lista.append(pessoas.copy())

    soma_idade += pessoas["idade"]

    opcao = input("Deseja continuar [S/N]? ")
    if opcao in "Nn":
        break
media = soma_idade / len(lista)

print(f"Total de pessoas cadastradas: {len(lista)}")

print(f"Média de idades: {media:.2f}")

print("Mulheres cadastradas: ", end="")
for i in lista:
    if i['sexo'] in "Ff":
        print(i["nome"], end=" ")

print("\nPessoas com idade acima da média: ")
for i in lista:
    if i["idade"] > media:
        print(f"{i['nome']} - {i['idade']} anos")
