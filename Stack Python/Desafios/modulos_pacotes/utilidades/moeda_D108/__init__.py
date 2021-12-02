def aumentar(n, a):
    """
    quantos % irá aumentar o preço
    :param n: preço
    :param a: taxa de aumento
    :return: retorna valor atualizado com a taxa
    """
    return (1+a/100) * n

def diminuir(n, a):
    return (1-a/100) * n

def dobro(n):
    return 2 * n

def metade(n):
    return n / 2

def moeda(preco, tipo = "R$"):
    return f"{tipo}{preco:.2f}".replace(".", ",")