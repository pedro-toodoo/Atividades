import pandas as pd

seriesAno1 = {'Python': 9.85, 'Java': 14.98, 'C++': 16.04}
seriesAno2 = {'Java': 17.35, 'C++': 12.67, 'Python': 11.56}

#1
dados1 = pd.Series(seriesAno1)
dados2 = pd.Series(seriesAno2)
print(dados1)

print(f"Nº 2:\nAno 1: {dados1.sum()}%\nAno 2: {dados2.sum():.2f}%")

dif = dados2 - dados1
print(f"Nº 3:\nCrescimento/declínio:\n{dif}")

print(f"Nº 4:\nInfo de linguagens com crescimento:\n{dif[dif > 0]}")

progressao = dif**2
print(f"Nº 5:\nCrescimento pra daqui 2 anos:\n{progressao[dif > 0]}\nDeclínio pra daqui 2 anos:\n{(progressao*-1)[dif<0]}")