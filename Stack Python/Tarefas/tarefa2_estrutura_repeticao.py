somaPeso = 0
somaAltura = 0

maisAlto = 0
maisBaixo = 10

maisGordo = 0
maisMagro = 500

cont = 0
while True:
    cod = int(input("Código: "))
    if cod == 0:
        break

    altura = float(input("Altura: "))
    peso = float(input("Peso: "))

    somaPeso += peso
    somaAltura += altura

    if altura > maisAlto:
        maisAlto = altura
        codAlto = cod

    if altura < maisBaixo:
        maisBaixo = altura
        codBaixo = cod

    if peso > maisGordo:
        maisGordo = peso
        codGordo = cod

    if peso < maisMagro:
        maisMagro = peso
        codMagro = cod
    cont += 1

print(f"Média de altura: {somaAltura / cont}")
print(f"Média de peso: {somaPeso / cont}")
print(f"Mais alto: {maisAlto} (Código: {codAlto})")
print(f"Mais baixo: {maisBaixo} (Código: {codBaixo})")
print(f"Mais Gordo: {maisGordo} (Código: {codGordo})")
print(f"Mais magro: {maisMagro} (Código: {codMagro})")
