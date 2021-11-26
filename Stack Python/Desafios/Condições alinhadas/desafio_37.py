num = int(input("Digite um número qualquer: "))

print("1 - conversão para binário")
print("2 - conversão para octal")
print("3 - conversão para hexadecimal")
opcao = int(input("Opção: "))

if opcao == 1:
    print(f"{num} em binário: {bin(num)}")
elif opcao == 2:
    print(f"{num} em octal: {oct(num)}")
elif opcao == 3:
    print(f"{num} em hexadecimal: {hex(num)}")
