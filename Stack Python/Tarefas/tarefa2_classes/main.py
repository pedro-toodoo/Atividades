from combustivel import *

tipo = input("Tipo do combustível: ")
while True:
    try:
        preco = float(input("Preço do combustível: R$"))
        break
    except Exception as erro:
        print(f"Entrada de dados inválida... Tente novamente! {erro}")
while True:
    try:
        qnt = int(input("Quantidade de combustível: "))
        break
    except Exception as erro:
        print(f"Entrada de dados inválida... Tente novamente! {erro}")

c1 = bombaCombustivel(tipo, preco, qnt)

while True:
    print("-"*30)
    print("INFORMAÇÕES DA BOMBA".center(30))
    print("-"*30)
    print(f"Tipo: {c1.tipoCombustivel}")
    print(f"Preço por litro: R${c1.valorLitro}")
    print(f"Quantidade de combustível: {c1.qntCombustivel}L")
    print("-"*30)
    print("1 - Abastecer por valor")
    print("2 - Abastecer por Litro")
    print("3 - Alterar valor do litro")
    print("4 - Alterar tipo do combustível")
    print("0 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Tipo de dado incorreto... Tente novamente")

    if opcao == 1:
        resp = c1.abastecerPorValor()
        c1.qntCombustivel = c1.alteraQntCombustivel(resp)
        print(f"Abastecido {resp}L")

    elif opcao == 2:
        preco = c1.abastecerPorLitro()  # retorna o preço
        l = preco / c1.valorLitro
        c1.qntCombustivel = c1.alteraQntCombustivel(l)
        print(f"Valor a pagar: R${preco}")

    elif opcao == 3:
        print(f"Novo valor: R${c1.alteraValor()}")

    elif opcao == 4:
        print(f"Novo tipo: {c1.alteraCombustivel()}")

    elif opcao == 0:
        print("Até logo...")
        break
    else:
        print("Opção não encontrado... Tente novamente")