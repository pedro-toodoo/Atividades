class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falando(self):
        print(f"{self.nomeclasse}: {self.nome} está falando...")


class Cliente(Pessoa): #herda de pessoa (cliente é pessoa)
    def comprar(self):
        print(f"{self.nomeclasse}: {self.nome} está comprando...")

class Aluno(Pessoa): #herda de pessoa (aluno é pessoa)
    def estudar(self):
        print(f"{self.nomeclasse}: {self.nome} está estudando...")
