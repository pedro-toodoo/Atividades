soma = 0
cont = 0
while True:
    num = int(input("Digite um valor (999 para parar): "))
    if num == 999:
        break
    soma += num
    cont += 1
print(f"Foram digitados {cont} valores \nSoma tota: {soma}")