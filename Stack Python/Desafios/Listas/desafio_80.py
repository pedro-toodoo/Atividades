lista = []
pos = 0

for i in range(0, 5):
    num = int(input("Digite um valor: "))

    if i == 0 or num > lista[-1]:
        lista.append(num)
    else:
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1

print(lista)
