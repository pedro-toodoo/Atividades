import random
from datetime import datetime

class Pessoa():
    ano_atual = int(datetime.strftime(datetime.now(), "%Y"))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade

    def get_ano_nasc(self): #método de instância
        print(self.ano_atual - self.idade)

    @classmethod #fabrica um objeto de classe (usado para especificar cada objeto) [é referente à classe]
    def por_ano_nasc(cls, nome, ano_nasc):
        idade = cls.ano_atual - ano_nasc
        return cls(nome, idade)

    @staticmethod #função normal só que fica dentro da classe. pra utilizar precisa usar instancia ou a classe
    def gerar_id():
        rand = random.randint(0, 10000)
        return rand

p1 = Pessoa.por_ano_nasc("Pedro", 1998)
#p1 = Pessoa("Pedro", 23)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nasc()

print(Pessoa.gerar_id())
print(p1.gerar_id())