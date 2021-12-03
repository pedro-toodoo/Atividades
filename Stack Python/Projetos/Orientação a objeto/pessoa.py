from datetime import datetime

class Pessoa():
    ano_atual = int(datetime.strftime(datetime.now(), "%Y"))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto): #self se refere à própria instância
        if self.comendo:
            print(f"{self.nome} não pode falar enquanto come...")
            return

        if self.falando:
            print(f"{self.nome} já está falando...")
            return

        print(f"{self.nome} está falando sobre {assunto}")
        self.falando = True

    def pararFalar(self):
        if not self.falando:
            print(f"{self.nome} não está falando...")
            return

        print(f"{self.nome} parou de falar...")
        self.falando = False


    def comer(self, comida):
        if self.comendo:
            print(f"{self.nome} já está comendo...")
            return

        if self.falando:
            print(f"{self.nome} não pode comer enquanto fala...")
            return

        print(f"{self.nome} está comendo {comida}...")
        self.comendo = True

    def pararComer(self):
        if not self.comendo:
            print(f"{self.nome} não está comendo...")
            return

        print(f"{self.nome} parou de comer!")
        self.comendo = False

    def get_ano_nasc(self):
        return self.ano_atual - self.idade
