import utilidades.dados as d
import utilidades.moeda_D110 as m

preco = d.leiaDinheiro("Digite o preço: R$")

print(f"{m.resumo(preco, 10, 15)}")