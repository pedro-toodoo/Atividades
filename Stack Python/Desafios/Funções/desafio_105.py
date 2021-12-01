def notas(*notas, s=False):
    """
    cria um dicionário com total de notas, a maior nota, menor nota, média das notas e a situação do aluno
    :param notas: todas as notas do aluno
    :param s: (opcional: default é false). Caso seja True irá mostrar a situação do aluno (boa, razoável, ruim)
    :return: sem retorno
    """
    dic ={"t_notas": "", "maior": "", "menor": "", "media": ""}
    maior = menor = soma =0

    # Quantidade de notas
    dic["t_notas"] = len(notas)

    # Maior e menor nota
    for i in range(0, len(notas)):
        if i == 0:
            maior = menor = notas[i]
        else:
            if notas[i] > maior:
                maior = notas[i]
            if notas[i] < menor:
                menor = notas[i]
    dic["maior"] = maior
    dic["menor"] = menor

    #soma das notas
    for i in range(0, len(notas)):
        soma += notas[i]
    media = soma / len((notas))
    dic["media"] = media

    if s == True:
        if media > 7.5:
            dic["situacao"] = "BOA"
        elif 6 <= media <= 7.5:
            dic["situacao"] = "RAZOÁVEL"
        elif media < 6:
            dic["situacao"] = "RUIM"
    print(dic)

notas(5,10,5, s=True)
