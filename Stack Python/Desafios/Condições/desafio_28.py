import random

num1 = int(input("Tente adivinhar o número escolhido pelo computador: "))

num2 = random.randint(0, 5)

if num1 == num2:
    print("Parabéns, você acertou!")
else:
    print("Azar, você errou!")