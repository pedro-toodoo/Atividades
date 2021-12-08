import numpy as np
import pandas as pd

data = {'Sede':['SP','SP','MG','MG','RJ','RJ','ES','ES'],
       'Vendedor':['Jorge','Ana','Tiago','Pedro','Raphaela','Guto','Maria','Carolina'],
       'Vendas':[2000,2500,3100,1200,1500,3900,2900,3900]}
df = pd.DataFrame(data)

print(df)

by_sede = df.groupby("Sede")
print(f"Agrupa sede por maiores vendas: \n{by_sede.max()}")
print(f"Agrupa sede por média: \n{by_sede.mean()}")
print(f"Visão geral: \n{by_sede.describe()}")
print(f"Invertendo linhas com colunas: \n{by_sede.describe().transpose()}")
print(f"Visão geral de uma única sede: \n{by_sede.describe().transpose()['MG']}")


arrays = [['São Paulo', 'São Paulo', 'Rio de Janeiro', 'Rio de Janeiro','Minas Gerais','Minas Gerais'],
['Garrafas','Copos','Garrafas','Copos','Garrafas','Copos' ]]
index = pd.MultiIndex.from_arrays(arrays, names=('Estado', 'Produto'))
df1 = pd.DataFrame({'Total Vendido R$': [10000, 35000, 22400, 12890,10880,13900]},index=index)

print()
print(df1)
by_estado = df1.groupby("Estado", level=0)

print(f"Agrupa por estado no nível 0: \n{by_estado.max()}")

by_produto = df1.groupby("Produto", level=1)

print(f"Agrupa por produto no nível 1: \n{by_produto.max()}")