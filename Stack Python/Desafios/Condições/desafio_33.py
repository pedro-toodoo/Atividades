num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if (num1 > num2) and (num1 > num3):
    print(f"Maior número: {num1}")
elif (num2 > num1) and (num2 > num3):
    print(f"Maior número: {num2}")
elif (num3 > num1) and (num3 > num2):
    print(f"Maior número: {num3}")

if (num1 < num2) and (num1 < num3):
    print(f"Menor número: {num1}")
elif (num2 < num1) and (num2 < num3):
    print(f"Menor número: {num2}")
elif (num3 < num1) and (num3 < num2):
    print(f"Menor número: {num3}")