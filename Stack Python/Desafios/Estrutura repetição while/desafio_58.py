import random

num2 = random.randint(0, 10)
num1 = ""

while num1 != num2:
    num1 = int(input("Tente adivinhar o número escolhido pelo computador: "))

print("Parabéns, você acertou!")