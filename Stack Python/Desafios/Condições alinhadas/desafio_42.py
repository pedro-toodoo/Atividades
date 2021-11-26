lado1 = int(input("Valor do lado 1: "))
lado2 = int(input("Valor do lado 2: "))
lado3 = int(input("Valor do lado 3: "))

if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
    if lado1 != lado2 != lado3 != lado1:
        print("Pode ser formado um triângulo ESCALENO!")
    elif lado1 == lado2 == lado3:
        print("Pode ser formado um triângulo EQUILÁTERO!")
    else:
        print("Pode ser formado um triângulo ISÓSCELES!")
else:
    print("Não pode ser formado um triângulo!")