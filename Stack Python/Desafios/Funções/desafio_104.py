def leiaInt():
    while True:
        num = input("Digite um número: ")
        if num.isnumeric():
            print(f"Número {num} aceito!")
            break
        else:
            print("ERRO. Aceita apenas números! ")

leiaInt()