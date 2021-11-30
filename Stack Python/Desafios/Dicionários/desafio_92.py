#aposenta com 35 anos de contribuição
from datetime import date

dic = {"nome": "", "idade": "", "trabalho": ""}

dic["nome"] = input("Nome: ")

ano_nasc = int(input("Data de nascimento: "))
ano_atual = date.today().year
dic["idade"] = ano_atual - ano_nasc

dic["trabalho"] = int(input("Número da carteira de trabalho: "))


if dic["trabalho"] == 0:
    for k, v in dic.items():
        print(f"{k} = {v}")

    print(f"Valor contido no dicionário: {dic}")
else:
    dic["contratacao"] = int(input("Ano de contratação: "))
    dic["salario"] = float(input("Salário: R$"))
    dic["aposentar"] = dic["contratacao"] + 35 - ano_atual + dic["idade"]
    for k, v in dic.items():
        print(f"{k} = {v}")

    print(f"Valor contido no dicionário: {dic}")