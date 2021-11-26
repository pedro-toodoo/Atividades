num = int(input("Digite o primeiro termo da PA: "))

razao = int(input("Digite a razão: "))
add = 10
total = 0

while add != 0:
    total = total + add
    while num <= total:
        print(num)
        num += razao
    add = int(input("Adicione mais números ou digite 0 para sair: "))
print(f"Foram mostrados {total} termos")


