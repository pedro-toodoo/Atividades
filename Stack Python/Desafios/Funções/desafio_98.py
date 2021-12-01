def contador(i, f, p):
    if i < f:
        if p < 0:
            print(f"Contagem de {i} até {f} com incremento de {p*-1}: ")
            for i in range(i, f+1, p* -1):
                print(f"{i}", end=" ")
            print()
        elif p > 0:
            print(f"Contagem de {i} até {f} com incremento de {p}: ")
            for i in range(i, f+1, p):
                print(f"{i}", end=" ")
            print()

    elif i > f:
        if p > 0:
            print(f"Contagem de {i} até {f} com decremento de {p}: ")
            for i in range(i, f-1, p* -1):
                print(f"{i}", end=" ")
            print()
        elif p < 0:
            print(f"Contagem de {i} até {f} com decremento de {p*-1}: ")
            for i in range(i, f-1, p):
                print(f"{i}", end=" ")
            print()

    if p == 0:
        if i < f:
            print(f"Contagem de {i} até {f} com incremento de 1: ")
            for i in range(i, f+1, 1):
                print(f"{i}", end=" ")
            print()

        elif i > f:
            print(f"Contagem de {i} até {f} com decremento de 1: ")
            for i in range(i, f-1, -1):
                print(f"{i}", end=" ")
            print()

contador(1, 11, 1)
contador(10, -1, -2)

print("Contagem personalizada:")
inicio = int(input("Início:"))
fim = int(input("Fim:"))
passo = int(input("Passo:"))
contador(inicio, fim, passo)


