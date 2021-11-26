num = int(input("Deseja ver a tabuada de qual valor (Digite um número negativo para sair? "))

while num >= 0:
    for i in range(0, 11):
        print(f"{num} * {i} = {num*i}")
    num = int(input("Deseja ver a tabuada de qual valor (Digite um número negativo para sair? "))
print("FIM!")