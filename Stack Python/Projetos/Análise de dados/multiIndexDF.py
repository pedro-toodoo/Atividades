import numpy as np
import pandas as pd

lista = [["BRASIL", "BRASIL", "BRASIL","ARGENTINA", "ARGENTINA", "ARGENTINA"], [2017, 2018, 2019, 2017, 2018, 2019]]
tuplas = zip(*lista) #junta

tuplas = list(tuplas)

multi = pd.MultiIndex.from_tuples(tuplas)

df1 = pd.DataFrame(data=np.random.randn(6, 2), index=multi, columns=["EXPORTAÇÃO DE CAFÉ", "EXPORTAÇÃO DE TRIGO"])

df1.index.names = ["PAÍS", "ANO"]
print(df1)

#encontrando valores:
print(df1.loc["BRASIL"])

print(df1.xs(2017, level=1))

#vendo dataframe de outra maneira:
print()
print(df1.unstack())

df2 = df1.unstack()

print(df2)
print(df2.xs(2017, axis=1, level=1)) #eixo e level




