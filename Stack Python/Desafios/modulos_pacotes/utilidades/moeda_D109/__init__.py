def aumentar(n=0, a=0, f=False):
    """
    quantos % irá aumentar o preço
    :param n: preço
    :param a: taxa de aumento
    :return: retorna valor atualizado com a taxa
    """
    novo = (1+a/100) * n

    if f == False:
        return novo
    else:
        return moeda(n)

def diminuir(n=0, a=0, f=False):
    novo = (1-a/100) * n

    if f == False:
        return novo
    else:
        return moeda(n)

def dobro(n=0, f=False):
    novo = 2 * n
    if f == False:
        return novo
    else:
        return novo

def metade(n=0, f=False):
    novo = n / 2
    if f == False:
        return novo
    else:
        return novo

def moeda(preco=0, tipo = "R$"):
    return f"{tipo}{preco:.2f}".replace(".", ",")