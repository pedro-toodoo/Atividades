import utilidades.moeda_D109 as m

preco = float(input("Digite o preço: R$"))

print(f"Aumento de 20% de {m.moeda(preco)} é {m.aumentar(preco, 20, True)}")
print(f"Redução de 15% de {m.moeda(preco)} é {m.diminuir(preco, 15, True)}")
print(f"O dobro de {m.moeda(preco)} é {m.dobro(preco)}")
print(f"A metade de {m.moeda(preco)} é {m.metade(preco)} ")