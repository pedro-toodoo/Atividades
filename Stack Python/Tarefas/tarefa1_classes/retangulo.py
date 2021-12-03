class Retangulo():
    def __init__(self, comp, larg):
        self.comp = comp
        self.larg = larg

    @classmethod
    def cria_por_medida(cls, comp, larg):
        return cls(comp, larg)

    def getMedidas(self):
        print(f"Comprimento: {self.comp} \tLargura: {self.larg}")

    def setMedidas(self, ladoA, ladoB):
        self.comp = ladoA
        self.larg = ladoB

    def calcArea(self):
        a = self.comp * self.larg
        return a

    def calcPerimetro(self):
        p = 2 * self.comp + 2 * self.larg
        return p
