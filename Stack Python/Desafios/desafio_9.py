num = int(input("Informe um número: "))

print(f"A tabuada de {num} é: ")
for i in range(0,11):
    print(f"{num}*{i} = {num*i}")