frase = input("Digite uma frase: ")

lista = frase.split()
#print(lista)

juntar = "".join(lista)
#print(juntar)

inverso = ""

for i in range(len(juntar) - 1, -1, -1):
    inverso = inverso + juntar[i]
#print(inverso)

if juntar == inverso:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")