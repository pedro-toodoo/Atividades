def fatorial(num, info=True):
    """
    informa o fatorial de um número com ou sem informações adicionais
    :param num: número para calcular fatorial
    :param info: parâmetro opcional para mostrar o fatorial detalhado (padrão True)
    :return: retorna o fatorial
    """
    fat = 1
    if info == True:
        for i in range(num, 0, -1):
            fat *= i
            if i > 1:
                print(f"{i} * ", end="")
            else:
                print(f"{i} = ", end="")

        print(fat)
        print(f"{num}! = {fat}")
    else:
        for i in range(num, 0, -1):
            fat *= i
        print(f"{num}! = {fat}")

num = int(input("Digite um número: "))
fatorial(num)