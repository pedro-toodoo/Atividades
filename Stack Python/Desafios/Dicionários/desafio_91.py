from random import randint
from time import sleep
from operator import itemgetter

dic = {"jogador1": "", "jogador2": "", "jogador3": "", "jogador4": ""}
ordem = {}

dic["jogador1"] = randint(1, 6)
dic["jogador2"] = randint(1, 6)
dic["jogador3"] = randint(1, 6)
dic["jogador4"] = randint(1, 6)

for k, v in dic.items():
    print(f"{k} = {v}")
    sleep(1)

ordem = sorted(dic.items(), key = itemgetter(1), reverse=True)

print("RANKING:")
for i, v in enumerate(ordem):
    print(f"{v[0]}: {i+1}º (Valor: {v[1]})")

