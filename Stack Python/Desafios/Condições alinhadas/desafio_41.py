from datetime import date

ano_nasc = int(input("Informe ano de nascimento do atleta: "))

ano_atual = date.today().year
idade = ano_atual - ano_nasc

if idade <= 9:
    print("Categoria: MIRIM")

elif idade > 9 and idade <= 14:
    print("Categoria: INFANTIL")

elif idade > 14 and idade <= 19:
    print("Categoria: JUNIOR")

elif idade == 20:
    print("Categoria: SÊNIOR")

elif idade > 20:
    print("Categoria: MESTRE")