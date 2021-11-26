from datetime import date

ano_nasc = int(input("Qual seu ano de nascimento? "))

ano_atual = date.today().year

idade = ano_atual - ano_nasc

if idade < 18:
    print(f"Você ainda se alistará no serviço militar daqui a {18-idade}!")
elif idade == 18:
    print("Está na hora de se alistar!")
elif idade > 18:
    print(f"Já se passaram {idade-18} anos desde seu alistamento!")