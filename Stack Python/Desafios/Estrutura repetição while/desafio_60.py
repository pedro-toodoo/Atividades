num = int(input("Digite um número: "))

fat = 1
cont = num
while cont != 1:
    fat = fat * cont
    cont -= 1

print(f"{num}! = {fat}")