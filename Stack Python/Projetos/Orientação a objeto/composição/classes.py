# UM OBJETO É DONO DE OUTRO
class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for v in self.enderecos:
            print(v.cidade, v.estado)

    def __del__(self): #garbage colector
        print(f"{self.nome} foi apagado")

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self): #garbage colector
        print(f"{self.cidade}({self.estado})")