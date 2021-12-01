def ficha(n="Qualquer", g=0):
    print(f"O jogador {n} fez {g} gol(s) no campeonato! ")

nome = input("Nome do jogador: ")
gols = input("Quantidade de gols: ")

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == "": #elimina os espaços e verifica se está vazio
    ficha(g=gols)
else:
    ficha(nome,int(gols))
