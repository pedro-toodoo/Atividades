times = ("Atlético MG", "Flamengo", "Palmeiras", "Corinthians", "Bragantino", "Fortaleza", "Fluminense", "Ceará SC", "Internacional", "América MG",
         "Santos", "São Paulo", "Cuiabá", "Athletico PR", "Atlético GO", "Bahia", "Juventude", "Grêmio", "Sport Recife", "Chapecoense")

print(f"5 primeiros colocados: {times[0:5]}")
print(f"4 últimos colocados: {times[-4:]}")
print(f"Times ordenados alfabeticamente: {sorted(times)}")
print(f"Fluminense está na posição {times.index('Fluminense')}")