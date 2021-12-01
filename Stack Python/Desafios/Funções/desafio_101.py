from datetime import date
ano_atual = date.today().year

def voto(a):
    """
    Informa se você pode ou não votar com base no seu ano de nascimento
    :param a: ano de nascimento
    :return: retorna mensagem informando se pode ou não
    """
    global idade
    idade = ano_atual - a
    if (idade == 18) or (idade >= 65):
        return "VOTO OPCIONAL"
    if idade > 18:
        return "VOTO OBRIGATÓRIO"
    if idade < 18:
        return "VOTO NEGADO"

ano = int(input("Data de nascimento: "))
resp = voto(ano)

print(f"Com {idade} anos: {resp}")