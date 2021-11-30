jogador = {}
partidas = []
time = []

while True:
    jogador["nome"] = input("Nome do jogador: ")
    qnt = int(input("Quantas partidas jogadas? "))
    partidas.clear()

    for i in range(1, qnt+1):
        partidas.append(int(input(f"    Quantidade de gols feitos na partida {i}: ")))

    jogador["partidas"] = partidas[:]
    jogador["total"] = sum(partidas)
    time.append(jogador.copy()) #salvando na lista time

    opcao = input("Deseja continuar [S/N]? ")
    if opcao in "Nn":
        break
    print("-"*20)

#print(time)

print("-"*20)
for i, valor in enumerate(time):
    print(f"{i:>4}", end=" ")
    for v in valor.values():
        print(f"{str(v):<15}", end="")
    print()
print("-"*20)

while True:
    cod = int(input("Qual código do jogador (-1 para sair)? "))
    if cod < 0:
        break
    if cod >= len(time):
        print(f"Não existe jogador {cod}. Tente novamente!")
    else:
        print(f"Dados do jogador {time[cod]['nome']}:")
        print("   Gols feitos em cada partida:")
        for i, v in enumerate(time[cod]["partidas"]):
            print(f"     Partida {i}: {v} gol(s)")




