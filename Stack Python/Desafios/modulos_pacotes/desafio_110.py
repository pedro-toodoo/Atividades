import utilidades.moeda_D110 as m

preco = float(input("Digite o preço: R$"))

print(f"{m.resumo(preco, 10, 15)}")