import numpy as np
import pandas as pd

#CONCATENATE melhor usado na vertical
#MERGE junta de várias formas how()

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])

dicionario = {'ID': [10, 11, 12, 13, 14, ], 'NOME': ['Mario', 'Joana', 'Claudia', 'Lucas', 'Gabriel'],
              'CIDADE': ['SÃO PAULO', 'RIO DE JANEIRO', 'SÃO PAULO', 'CAMPINAS', 'PORTO ALEGRE']}
dicionario2 = {'ID': [16, 11, 12, 13, 18, ], 'Experiência': ['Junior', 'Senior', 'Pleno', 'Estagiário', 'Analista']}

df4 = pd.DataFrame(data=dicionario)
df5 = pd.DataFrame(data=dicionario2)

dicionario3 = {'NOME':['Mario','Joana','Claudia','Lucas','Gabriel'],
              'CIDADE':['SÃO PAULO','RIO DE JANEIRO','SÃO PAULO','CAMPINAS','PORTO ALEGRE']}

dicionario4 = {'Experiência':['Junior','Senior','Pleno','Estagiário','Analista']}

df7 = pd.DataFrame(data=dicionario3)
df8 = pd.DataFrame(data=dicionario4)

print(df1)
print()
print(df2)
print()
print(df3)
print()

#concatenate
print(f"Concatenando DF1 com DF2: \n{pd.concat([df1, df2])}")

print()
print(df4)
print()
print(df5)
print()

#MERGE une através de coluna
#merge inner (padrão): junta apenas os que tem ID igual
print(f"Merge com INNER DF4 e DF5: \n{pd.merge(df4, df5)}")

#merge outer: junta tds os valores e coloca nulo nos que não tem correspondência
print(f"Merge COM OUTER DF4 e DF5: \n{pd.merge(df4, df5, how='outer')}")

#merge left: todos valores da esquerda estão presentes
print(f"Merge COM LEFT DF4 e DF5: \n{pd.merge(df4, df5, how='left')}")

#merge right: todos valores da direita estão presentes
print(f"Merge COM RIGHT DF4 e DF5: \n{pd.merge(df4, df5, how='right')}")

#JOIN: unir índices
print(f"Join errado: \n{df4.join(df5, lsuffix='_X', rsuffix='_Y')}")
print(f"Join por índices: \n{df7.join(df8)}")




