dist = int(input("Qual a distância em Km? "))

if dist <= 200:
    print(f"O preço da passagem é de R${dist*0.5}")
else:
    print(f"O preço da passagem é de R${dist * 0.45}")