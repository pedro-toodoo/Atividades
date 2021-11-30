jogador = {"nome": input("Nome do jogador: "), "partidas": [], "total": 0}
partidas = []

qnt = int(input("Quantas partidas jogadas? "))
soma = 0

for i in range(1, qnt+1):
    partidas.append(int(input(f"Quantidade de gols feitos na partida {i}: ")))
    jogador["total"] = sum(partidas)

jogador["partidas"] = partidas[:]
#print(partidas)
#print(f"{jogador}")

print(f"Nome do jogador: {jogador['nome']}")
print(f"Quantidade de partidas jogadas no campeonato: {qnt}")
print(f"Total de gols no campeonado: {jogador['total']}")
print("Informações das partidas: ")
for i, valor in enumerate(partidas):
    print(f"Partida {i+1}: {valor} gols")




