soma = 0
qnt = 0
barato = 99999
nome_barato = ""
while True:
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    opcao = input("Deseja continuar (S ou N)? ")

    soma += preco
    if preco > 1000:
        qnt += 1
    if preco < barato:
        nome_barato = nome

    if opcao == 'N':
        break
print(f"Total gasto na compra: R${soma}")
print(f"Quantidade de produtos acima de R$1000: {qnt}")
print(f"Nome do produto mais barato: {nome_barato}")


