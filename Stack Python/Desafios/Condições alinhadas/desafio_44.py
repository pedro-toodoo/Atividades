preco = float(input("Valor do produto: R$"))

print("1 - À vista no dinheiro")
print("2 - À vista no cartão")
print("3 - 2x no cartão")
print("4 - 3x ou mais no cartão")
opcao = int(input("Opção: "))

if opcao == 1:
    print(f"Valor com 10% de desconto: R${0.9 * preco}")

if opcao == 2:
    print(f"Valor com 5% de desconto: R${0.95 * preco}")

if opcao == 3:
    print(f"Valor com preço normal: R${preco}")

if opcao == 4:
    print(f"Valor com 20% de juros: R${1.2 * preco}")