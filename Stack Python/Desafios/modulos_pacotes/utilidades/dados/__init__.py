def leiaDinheiro(preco):
    aux = False
    while not aux:
        entrada = str(input(preco).replace(",", "."))
        if entrada.isalpha() or entrada.strip() == "":
            print(f"ERRO. '{entrada}' não é válido!")
        else:
            aux = True
            return float(entrada)