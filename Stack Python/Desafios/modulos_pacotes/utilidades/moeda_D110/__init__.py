def aumentar(preco=0, taxa=0, f=False):
    """
    quantos % irá aumentar o preço
    :param n: preço
    :param a: taxa de aumento
    :return: retorna valor atualizado com a taxa
    """
    novo = (1+taxa/100) * preco

    if f == False:
        return novo
    else:
        return moeda(preco)

def diminuir(preco=0, taxa=0, f=False):
    novo = (1-taxa/100) * preco

    if f == False:
        return novo
    else:
        return moeda(preco)

def dobro(preco=0, f=False):
    novo = 2 * preco
    if f == False:
        return novo
    else:
        return novo

def metade(preco=0, f=False):
    novo = preco / 2
    if f == False:
        return novo
    else:
        return novo

def moeda(preco=0, tipo = "R$"):
    return f"{tipo}{preco:.2f}".replace(".", ",")

def resumo(preco, t_aumento, t_reducao):
    print("RESUMO DO VALOR".center(30))
    print("-"*30)
    print(f"Analisado: {moeda(preco)}")
    print(f"Dobro: {moeda(preco)}")
    print(f"Metade: {moeda(preco)}")
    print(f"{t_aumento}% de aumento: {moeda(preco)}")
    print(f"{t_reducao}% de redução: {moeda(preco)}")