class bombaCombustivel():
    def __init__(self, tipoCombustivel, valorLitro, qntCombustivel):
        self.tipoCombustivel = str(tipoCombustivel)
        self.valorLitro = float(valorLitro)
        self.qntCombustivel = int(qntCombustivel)

    def abastecerPorValor(self):
        while True:
            try:
                valor = float(input("Informe o valor para abastecer: R$"))
            except:
                print("Valor não aceito... Tente novamente")

            else:
                qnt_abastecida = valor / self.valorLitro
                return qnt_abastecida

    def abastecerPorLitro(self):
        while True:
            try:
                qnt = int(input("Informe a quantidade que deseja abastecer (L): "))
            except:
                print("Valor não aceito... Tente novamente")
            else:
                preco = qnt * self.valorLitro
                return preco

    def alteraValor(self):
        while True:
            try:
                altera_valor = float(input("Novo valor do litro: R$"))
            except:
                print("Valor não aceito... Tente novamente")
            else:
                self.valorLitro = altera_valor
                return self.valorLitro

    def alteraCombustivel(self):
        while True:
            try:
                altera_tipo = input("Novo combustível: ")
            except:
                print("Valor não aceito... Tente novamente")
            else:
                self.tipoCombustivel = altera_tipo
                return self.tipoCombustivel

    def alteraQntCombustivel(self, qnt):
        if self.qntCombustivel >= qnt:
            self.qntCombustivel -= qnt
            return self.qntCombustivel
        else:
            print(f"Impossível retirar {qnt}L da bomba...")
            self.qntCombustivel = self.qntCombustivel
            return self.qntCombustivel
