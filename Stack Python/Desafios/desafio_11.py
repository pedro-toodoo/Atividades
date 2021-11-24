altura = float(input("Qual a altura da parede? "))
largura = float(input("Qual a largura da parede? "))
area = altura*largura
print(f"Área da parede: {area}m²")

print("(Assumindo que 1L de tinta é capaz de pintar uma área de 2m²)")

print("Serão gasto(s) {:.1f}L de tinta".format(area/2))