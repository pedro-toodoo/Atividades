"""
_ protected (variáveis com _ antes do nome não devem ser acessadas fora da classe)
__ privado (não quer que o atributo/método seja acessado) [_NOMECLASSE__nomeatributo]
"""

class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for k, v in self.__dados['clientes'].items():
            print(f"{k}: {v}")

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_cliente(1, "Pedro")
bd.inserir_cliente(2, "homem aranha")
bd.inserir_cliente(3, "Dr. Octopus")
bd.lista_clientes()

print("-"*10)
bd.__dados = "Qualquer coisa"
print(bd.__dados)
#para acessar os dados privados:
print(bd._BaseDeDados__dados)