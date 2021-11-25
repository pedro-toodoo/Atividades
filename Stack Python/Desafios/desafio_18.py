from math import cos, sin, tan, radians

a = float(input("Digite um ângulo qualquer: "))

print("Valores em graus: ")
print("Seno = {:.2f}".format(sin(radians(a))))
print("Cosseno = {:.2f}".format(cos(radians(a))))
print("Tangente = {:.2f}".format(tan(radians(a))))