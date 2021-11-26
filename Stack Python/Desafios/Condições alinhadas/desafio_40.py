nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota2 + nota1) / 2

if media < 5.0:
    print("Reprovado :(")
elif media >= 5.0 and media <= 6.9:
    print("Recuperação :/")
elif media > 7.0:
    print("Aprovado :)")