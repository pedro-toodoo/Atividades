ano = int(input("Ano para verificação: "))

if (ano % 4 == 0) and (ano % 100 != 0) and (ano % 400 == 0):
    print(f"Ano de {ano} é BISSEXTO!")
else:
    print(f"Ano de {ano} não é BISSEXTO!")