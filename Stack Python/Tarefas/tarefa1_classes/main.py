from retangulo import *

c = float(input("Informe o comprimento: "))
l = float(input("Informe a largura: "))

r1 = Retangulo.cria_por_medida(c, l)

r1.getMedidas()
print(f"Área do retângulo: {r1.calcArea()}m²")
print(f"Perímetro do retângulo: {r1.calcPerimetro()}m")

c2 = float(input("Altere o comprimento: "))
l2 = float(input("Altere a largura: "))
r1.setMedidas(c2, l2)
print("NOVAS MEDIDAS:")
r1.getMedidas()
print(f"Área total para compra dos pisos: {r1.calcArea()}m²")
print(f"Perímetro total para fazer os rodapés: {r1.calcPerimetro()}m")