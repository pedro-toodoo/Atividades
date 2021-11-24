#Type() mostra o valor primitivo da variável (objeto)
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
print(f"A soma de {num1} e {num2} é igual a {num1+num2}")

#outro formato de print que funciona igual acima:
print("A soma de {} e {} é igual a {}".format(num1, num2, num1 + num2))
