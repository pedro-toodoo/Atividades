qnt18 = 0
qntM = 0
qntF20 = 0
while True:
    idade = int(input("Idade: "))
    sexo = input("Sexo (M ou F): ")
    opcao = input("Deseja continuar (S ou N)? ")

    if idade > 18:
        qnt18 += 1
    if sexo == "M":
        qntM += 1
    if idade < 20 and sexo == 'F':
        qntF20 += 1

    if opcao == 'N':
        break
print(f"Quantidade de pessoas acima de 18 anos: {qnt18}")
print(f"Quantidade de homens cadastrados: {qntM}")
print(f"Quantidade de mulheres abaixo dos 20: {qntF20}")


