from .interfaces import Ihabilidade

class Curar(Ihabilidade):

    def __init__(self, nivel):
        self.nivel = nivel
    
    def comportamento(self):
        print("Curar aliado")
    
    def nivel_atributo(self):
        print(f"Nível de uso de cura: {self.nivel}")

    