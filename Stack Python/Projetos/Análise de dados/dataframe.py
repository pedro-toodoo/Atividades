import pandas as pd
import numpy as np

#criando dataframe a partir de um array:
arr = np.random.randint(10, 55, size=(4,4))
print(arr)

df1 = pd.DataFrame(data=arr, index=["A", "B", "C", "D"], columns=["W", "X", "Y", "Z"])
print(df1)

#criando dataframe a partir de listas:
lista = [[10, 20, 30, 40], [50, 60, 70, 80]] #lista dentro de lista
df2 = pd.DataFrame(data=lista)
print(df2)

#criando dataframe a partir de dicionário:
dados = {"Produtos": ["videogame", "PC", "teclado", "mouse", "mic"], "preço": [2600, 2450, 99.9, 75, 124.9]}
df3 = pd.DataFrame(data=dados)
df3['custo'] = [1900, 2000, 40, 50.9, 95]
df3["lucro"] = df3['preço'] - df3["custo"]
print(df3) 