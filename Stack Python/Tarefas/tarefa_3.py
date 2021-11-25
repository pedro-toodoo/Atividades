frase1 = input("Digite uma frase: ")
frase2 = input("Digite outra frase: ")

print(f"Tamanho de '{frase1}': {len(frase1)}")
print(f"Tamanho de '{frase2}': {len(frase2)}")

if len(frase1) == len(frase2):
    print("As duas strings são do mesmo tamanho")
else:
    print("As duas strings são de tamanhos diferentes")

if frase1 == frase2:
    print("As duas strings possuem o mesmo conteúdo!")
else:
    print("As duas strings possuem conteúdo diferente!")