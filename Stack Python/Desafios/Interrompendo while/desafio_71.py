saque = int(input("Qual valor será sacado? "))
nota = 50
resto = saque
cont = 0
while True:
    if resto >= nota:
        resto -= nota
        cont += 1
    else:
        print(f"Total de notas de R${nota}: {cont}")
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        cont = 0
        if resto == 0:
            break;