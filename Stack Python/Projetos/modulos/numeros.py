from uteis import numeros

num = int(input("Digite um número: "))
resp = numeros.fatorial(num)

print(f"informações de {num}: ")
print(f"Fatorial: {resp}")
print(f"Dobro: {numeros.dobro(num)}")
print(f"Triplo: {numeros.triplo(num)}")

