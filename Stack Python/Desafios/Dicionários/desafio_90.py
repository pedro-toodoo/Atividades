dic = {"nome": "", "media": "", "situacao": ""}

dic["nome"] = input("Nome: ")
dic["media"] = float(input("Média: "))

if dic["media"] >= 6:
    dic["situacao"] = "Aprovado"
elif 3 <= dic["media"] < 6:
    dic["situacao"] = "Recuperação"
elif dic["media"] < 3:
    dic["situacao"] = "Reprovado"

for k, v in dic.items():
    print(f"{k} = {v}")