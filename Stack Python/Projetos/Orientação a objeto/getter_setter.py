class Produto():

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (percentual * self.preco / 100)

    #Getter
    @property
    def preco(self):
        return self._preco

    #Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace("R$", ""))

        self._preco = valor

    #Getter
    @property
    def nome(self):
        return self._nome

    #Setter
    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()


p1 = Produto("FACA", 10)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto("boi", "R$50")
p2.desconto(50)
print(p2.nome, p2.preco)