from classes import *

carrinho = CarrinhoDeCompras()
p1 = Produto("camiseta", 25)
p2 = Produto("PS5", 5000)
p3 = Produto("meia", 5)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p2)
carrinho.lista_produto()

print(f"Valor a ser pago: R${carrinho.soma_total():.2f}")