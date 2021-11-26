valor = float(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salário? "))
anos = int(input("Em quantos anos quer financiar? "))

prestacao = valor / anos

if prestacao <= 0.3*salario:
    print(f"Empréstimo aprovado! Mensalidade de {prestacao} por {anos} anos!")
else:
    print("Infelizmente o empréstimo foi recusado!")