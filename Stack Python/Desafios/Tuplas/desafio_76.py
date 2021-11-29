tupla = ("Mouse", 90, "Teclado", 100, "Headset", 110, "Webcam", 80, "Placa de vídeo", 1500, "Monitor", 450, "Processador", 1300)

print("*"*30)
print(f"{'LISTAGEM DE PREÇOS':^30}")
print("*"*30)

for i in range(0, len(tupla)):
    if i % 2 == 0:
        print(f"{tupla[i]:.<20}", end=" R$")
    else:
        print(f"{tupla[i]:.2f}")