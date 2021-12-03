def imprime(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print(f"{j+1}", end=" ")
        print()

num = int(input("Digite um número: "))
imprime(num)

