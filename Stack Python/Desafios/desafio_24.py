nome = input("Qual nome da sua cidade? ")
aux = nome.upper()

lista = aux.split()

if "SANTO" == lista[0]:
    print("Sua cidade começa com a palavra SANTO")
else:
    print("Sua cidade não começa com a palavra SANTO")