salario = float(input("Qual seu salário? R$"))

if salario > 1250:
    print(f"Aumento de 10%, logo o novo salário é de R${1.1*salario}")
else:
    print(f"Aumento de 15%, logo o novo salário é de R${1.15 * salario}")