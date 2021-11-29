
tupla = (int(input("Digite um valor: ")), int(input("Digite um valor: ")), int(input("Digite um valor: ")),
         int(input("Digite um valor: ")))

print(f"Vezes que apareceu o número 9: {tupla.count(9)}")
print(f"Posição da primeira aparição do número 3: {tupla.index(3)}")

print("Números pares encontrados: ", end="")
for i, pos in enumerate(tupla):
    if i % 2 == 0:
        print(i)