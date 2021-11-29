expressao = input("Digite uma expressão: ")



for pos, valor in enumerate(expressao):
    aux = " ".join(expressao)
    lista = aux.split()
print(lista)

x = lista.count("(")
y = lista.count(")")

#print(x)
#print(y)

if x == y:
    print("Expressão correta! ")
else:
    print("Expressão incorreta! ")