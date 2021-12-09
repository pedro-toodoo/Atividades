from retangulo import *

while True:
    try:
        c = float(input("Informe o comprimento: "))
        break
    except Exception as erro:
        print(f"Entrada de dados inválida... Tente novamente! {erro}")
while True:
    try:
        l = float(input("Informe a largura: "))
        break
    except Exception as erro:
        print(f"Entrada de dados inválida... Tente novamente! {erro}")

r1 = Retangulo.cria_por_medida(c, l)

r1.getMedidas()
print(f"Área do retângulo: {r1.calcArea()}m²")
print(f"Perímetro do retângulo: {r1.calcPerimetro()}m")

while True:
    try:
        c2 = float(input("Informe o comprimento: "))
        break
    except Exception as erro:
        print(f"Entrada de dados inválida... Tente novamente! {erro}")
while True:
    try:
        l2 = float(input("Informe a largura: "))
        break
    except Exception as erro:
        print(f"Entrada de dados inválida... Tente novamente! {erro}")

r1.setMedidas(c2, l2)

print("NOVAS MEDIDAS:")
r1.getMedidas()
print(f"Área total para compra dos pisos: {r1.calcArea()}m²")
print(f"Perímetro total para fazer os rodapés: {r1.calcPerimetro()}m")