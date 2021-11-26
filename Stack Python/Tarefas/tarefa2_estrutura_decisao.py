nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota2 + nota1) / 2

if media >= 9 and media <= 10:
    print("Nota: A")
    print(f"Média: {media}")
    print("Aprovado")

elif media >= 7.5 and media < 9:
    print("Nota: B")
    print(f"Média: {media}")
    print("Aprovado")

elif media >= 6 and media < 7.5:
    print("Nota: C")
    print(f"Média: {media}")
    print("Aprovado")

elif media >= 4 and media < 6:
    print("Nota: D")
    print(f"Média: {media}")
    print("Reprovado")
elif media >= 0 and media < 4:
    print("Nota: E")
    print(f"Média: {media}")
    print("Reprovado")