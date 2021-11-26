import random

pc = random.randint(0, 10)
soma = 0
cont = 0
opcao = int(input("1 - Par\n2 - Ímpar\nOpção: "))
num = int(input("Digite um número entre 0 e 10: "))

soma = pc + num

while True:
    if opcao == 1:
        if soma % 2 == 0:
            print(f"Você jogou {num} / Computador jogou {pc}\nResultado par: {soma}\nVocê ganhou!")
            cont += 1
        else:
            print(f"Você jogou {num} / Computador jogou {pc}\nResultado ímpar: {soma}\nVocê perdeu!")
            break
    elif opcao == 2:
        if soma % 2 == 0:
            print(f"Você jogou {num} / Computador jogou {pc}\nResultado par: {soma}\nVocê perdeu!")
            break
        else:
            print(f"Você jogou {num} / Computador jogou {pc}\nResultado ímpar: {soma}\nVocê ganhou!")
            cont += 1

    opcao = int(input("1 - Par\n2 - Ímpar\nOpção: "))
    num = int(input("Digite um número entre 0 e 10: "))
    pc = random.randint(0, 10)
    soma = pc + num
print(f"Você ganhou {cont} vez(es)")
print("GAME OVER")