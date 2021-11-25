from math import sqrt

c1 = float(input("Digite o valor do cateto oposto: "))
c2 = float(input("Digite o valor do cateto adjacente: "))

hip = sqrt((pow(c1, 2) + (pow(c2, 2))))

print("O comprimento da hipotenusa é: {:.2f}".format(hip))