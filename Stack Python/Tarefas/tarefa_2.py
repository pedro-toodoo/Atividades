peso = float(input("Peso em Kg da quantidade de peixes: "))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f"Mercadoria com {excesso}Kg de excesso!")
    print(f"Multa de R${multa}!")
else:
    print("Mercadoria abaixo do regulamento! OK")