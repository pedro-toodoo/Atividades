from datetime import date

data = date.today().year
maioridade = 0
menor = 0
for i in range(0, 7):
    ano = int(input("Digite seu ano de nascimento: "))
    if data - ano >= 18:
        maioridade += 1
    else:
        menor += 1
print(f"{maioridade} pessoas são de maior!")
print(f"{menor} pessoas são de menor!")