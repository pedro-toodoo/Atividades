def fatorial(num):
    """
    faz o fatorial de um número
    :param num: número que será calculado o fatorial
    :return: retorna o fatorial de "num"
    """
    fat = 1
    for i in range(1, num+1):
        fat *= i
    #print(f"{num}! = {fat}")
    return fat

n = int(input("Digite um número: "))
fatorial(n)
