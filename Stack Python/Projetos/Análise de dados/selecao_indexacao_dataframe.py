import pandas as pd
import numpy as np
np.random.seed(100)

indices = ["janeiro", "março", "maio", "julho", "agosto", "outubro", "dezembro"]
colunas = np.arange(1, 32)
dados = np.random.randint(492, 2050, size=(7, 31))

df = pd.DataFrame(data=dados, index=indices, columns=colunas)
# df[:2] PEGA AS LINHAS
#print(df[:2])

print(df)
"""
df[coluna]
df[[col1, col2, col3]]
df[coluna][linha]
df[linha1:linha2]
df.loc[indice linha, indice coluna]
df.iloc[ind num linha, ind, num coluna] df.iloc[3,30]
df.loc[[ind1, ind2, ind3], [col1, col2, col3]]
"""

# retorna tudo do dia 10, 20 e 30
print(df[[10, 20, 30]])

#quanto vendeu 14 de março:
print(df[14]["março"])

#quanto vendeu em janeiro, março e maio:
print(df[:3])

#quanto vendeu em julho, agosto e outubro do dia 25 até 31:
print(df.loc[["julho", "agosto", "outubro"],[25, 26, 27, 28, 29, 30, 31]])
print(df.iloc[[3, 4, 5], [24, 25, 26, 27, 28, 29, 30]])

#trocar nome:
df.rename({"dezembro":"teste"}, inplace=True)

#valores abaixo de 1000 ficam com "-"
print(df[df > 1000].fillna("-"))

#[condição][linha][coluna]
print(df[df > 1000][:][[1, 2, 3, 4, 5]].fillna("-")) #se quiser + de 1 coluna tem q passar outra lista [[]]

#varias condições:
print()
print(df[(df[10] > 1000) & (df[15] > 1500)])







