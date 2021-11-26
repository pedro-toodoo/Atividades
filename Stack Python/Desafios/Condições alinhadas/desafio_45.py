import random

print("0 - Pedra")
print("1 - Papel")
print("2 - Tesoura")
lista = ["Pedra", "Papel", "Tesoura"]
opcao = int(input("Escolha pedra, papel ou tesoura: "))

pc = random.randint(0, 2)

print(f"Você jogou {lista[opcao]} e o computador jogou {lista[pc]}")

if opcao == 0 and pc == 0:
    print("Empate!")
elif opcao == 0 and pc == 1:
    print("Computador ganhou!")
elif opcao == 0 and pc == 2:
    print("Você ganhou! ")

elif opcao == 1 and pc == 1:
    print("Empate!")
elif opcao == 1 and pc == 2:
    print("Computador ganhou!")
elif opcao == 1 and pc == 0:
    print("Você ganhou! ")

elif opcao == 2 and pc == 2:
    print("Empate!")
elif opcao == 2 and pc == 1:
    print("Computador ganhou!")
elif opcao == 2 and pc == 0:
    print("Você ganhou! ")