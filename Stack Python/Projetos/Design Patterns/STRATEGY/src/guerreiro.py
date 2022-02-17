from .habilidades import Ihabilidade
from typing import Type

class Guerreiro:

    def __init__(self, habilidade: Type[Ihabilidade]):
        self.habilidade = habilidade

    def acao(self):
        self.habilidade.comportamento()
      
    def atributos(self):
        #print(f"Nivel Arco: {self.habilidade_arco}\nNivel cura: {self.habilidade_cura}\nNivel Luta: {self.habilidade_luta}")
        self.habilidade.nivel_atributo()  