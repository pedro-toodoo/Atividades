dados = []

dados.append("Pedro")
dados.append(23)

print(dados)
print(dados[0])
print(dados[1])

pessoas = []

pessoas.append(dados[:]) #fatiamento completo (cópia de dados
print(pessoas)

pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]

print(pessoas)
print(pessoas[2][0])