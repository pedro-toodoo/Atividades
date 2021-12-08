import pandas as pd
import numpy as np

df = pd.read_csv("campeonato-brasileiro-full.csv")
print(df.head(5))

print(f"Informações: \n{df.info()}")
print(f"Média de gols do time mandante:{df['Mandante Placar'].mean():.2f}")

df["Total Gols"] = df["Mandante Placar"] + df["Visitante Placar"]
print(f"Média de gols: {df['Total Gols'].mean():.2f}")

df["Vencedor"] = df["Vencedor"].str.upper() #transformando tudo para maiúsculo
print(f"Times que mais ganharam: {df['Vencedor'].value_counts()}")

print(f"Estados que mais ganharam: {df['Estado Vencedor'].value_counts()}")


print(f"Ordenar maiores goleadas: {df.sort_values(by='Mandante Placar', ascending=False)}")

df['Mandante'] = df['Mandante'].str.upper()
print(f"Valores únicos de uma coluna: {df['Mandante'].unique()}")

df['Visitante'] = df['Visitante'].str.upper()
print(f"Quantidade de times visitantes únicos: {df['Visitante'].nunique()}")

print(f"Maior goleada: \n{df['Mandante Placar'][df['Mandante Placar'] == df['Mandante Placar'].max()]}")


by_mandante = df.groupby('Mandante')
print(f"Time que fez mais gols: {by_mandante['Mandante Placar'].sum().sort_values(ascending=False)}")



