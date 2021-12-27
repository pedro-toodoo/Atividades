import pandas as pd

#1
seriesAno1 = {'Python': 9.85, 'Java': 14.98, 'C++': 16.04}
seriesAno2 = {'Java': 17.35, 'C++': 12.67, 'Python': 11.56}
#df = pd.DataFrame(data=seriesAno1)
print(f"ANO 1:\n{pd.Series(seriesAno1)}")
print(f"ANO 2:\n{pd.Series(seriesAno2)}\n")

#2
total1 = total2 = 0
for k, v in seriesAno1.items():
    total1 += v
print(f"Porcentagem no ano 1: {total1}%")

for k, v in seriesAno2.items():
    total2 += v
print(f"Porcentagem no ano 2: {total2:.2f}%\n")

#3
for k, v in seriesAno1.items():
    for key, value in seriesAno2.items():
        if key == k:
            if value > v:
                print(f"{k} teve um crescimento de {(value-v):.2f}%")
            elif value < v:
                print(f"{k} teve um declínio de {(v-value):.2f}%")

#4
print("\nDados de crescimento:")
for k, v in seriesAno1.items():
    for key, value in seriesAno2.items():
        if key == k:
            if value > v:
                print(f"{k}: Ano 1: {v}% / Ano 2: {value}%")

#5








