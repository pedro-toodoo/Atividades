num = int(input("Quantidade de termos da sequência de Fibonacci: "))

fib1 = 0
fib2 = 1
cont = 3 # já tem os 2 primeiros termos (0 e 1)
print(f"{fib1} -> {fib2}", end="")

while cont <= num:
    soma = fib1 + fib2
    fib1 = fib2
    fib2 = soma
    cont += 1
    print(f" -> {fib2}", end="")

