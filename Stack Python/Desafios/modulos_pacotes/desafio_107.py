import mo

preco = float(input("Digite o preço: R$"))

print(f"Aumento de 20% de R${preco} é R${m.aumentar(preco, 20)}")
print(f"Redução de 15% de R${preco} é R${m.diminuir(preco, 15)}")
print(f"O dobro de R${preco} é R${m.dobro(preco)}")
print(f"A metade de R${preco} é R${m.metade(preco)} ")