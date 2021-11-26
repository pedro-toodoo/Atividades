opcao = ""
soma = 0
cont = 1
maior = 0
menor = 9999999
while opcao != 'N':
    num = int(input("Digite um número: "))
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    cont += 1
    opcao = input("Deseja continuar? S ou N  ")

print(f"Média: {soma / cont}")
print(f"maior: {maior}")
print(f"Menor: {menor}")
