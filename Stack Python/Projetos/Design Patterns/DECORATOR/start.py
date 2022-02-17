def decorator(funcao):
    def wrapper(args, **kwargs): #funcao_superior
        print('Alô mundo')
        funcao(args, **kwargs)
    return wrapper

@decorator
def minha_funcao():
    print("Fala cmg aqui dentro da função!")


class minha_classe:

    @decorator
    def metodo(self):
        print("Estou na minha classe")

    @decorator
    def metodo2(self):
        print("teste algum")
    

cl = minha_classe()
cl.metodo()
cl.metodo2()