soma = 0
mulher = 0
maior_idade = 0
velho = ""
for i in range(0, 4):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (m ou f): ")

    soma += idade
    if sexo == 'f' and idade < 20:
        mulher += 1
    if idade > maior_idade and sexo == 'm':
        velho = nome

print(f"Média das idades: {soma / 4}")
print(f"Nome do homem mais velho: {velho}")
print(f"Quantidade de mulheres com menos de 20 anos: {mulher}")