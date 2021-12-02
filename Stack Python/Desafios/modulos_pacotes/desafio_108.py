import utilidades.moeda_D108 as m

preco = float(input("Digite o preço: R$"))

print(f"Aumento de 20% de {m.moeda(preco)} é {m.moeda(m.aumentar(preco, 20))}")
print(f"Redução de 15% de {m.moeda(preco)} é {m.moeda(m.diminuir(preco, 15))}")
print(f"O dobro de {m.moeda(preco)} é {m.moeda(m.dobro(preco))}")
print(f"A metade de {m.moeda(preco)} é {m.moeda(m.metade(preco))} ")