from .interfaces import Ihabilidade

class LutaArco(Ihabilidade):

    def __init__(self, nivel):
        self.nivel = nivel
    
    def comportamento(self):
        print("Atirar flechas")
    
    def nivel_atributo(self):
        print(f"Nível de uso do arco: {self.nivel}")

    