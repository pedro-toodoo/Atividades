from classes import *

c1 = Cliente("Pedro", 23)
c1.insere_endereco("Cataguases", "MG")
print(c1.nome)
c1.lista_enderecos()
del c1
print()

c2 = Cliente("José", 24)
c2.insere_endereco("Juíz de Fora", "MG")
c2.insere_endereco("São Paulo", "SP")
print(c2.nome)
c2.lista_enderecos()
del c2
print()

print("-"*30)