def mensagem(m):
    print("-"*20)
    print(m)
    print("-"*20)

def soma(a, b):
    s = a + b
    print(f"Soma: {s}")

#desempacotamento:
def contador(*num):
    #cria uma tupla
    print(f"Valores:", end=" ")
    for v in num:
        print(f"{v}", end=" ")

#dobrar valores da lista:
def dobra(lst):
    for i in range(0, len(lst)):
        lst[i] *= 2

mensagem("   Fala cmg bb")
soma(1, 3)
soma(b=10, a=20)
contador(1, 2, 3, 4, 9)

lista = [1, 2, 3, 4, 5, 6]
dobra(lista)
print(lista)