maior = 0
menor = 9999

for i in range(0, 5):
    peso = float(input("Qual seu peso? "))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
        
print(f"Maior peso: {maior}")
print(f"Menor peso: {menor}")