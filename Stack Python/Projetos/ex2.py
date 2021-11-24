#função isnumeric() retorna se é possível converter o valor de input para número
#função isalnum() retorna se é possível converter o valor de input para alpha numérico
#função isalpha() retorna se é possível converter o valor de input para string
info = input("Digite qualquer coisa para apresentar as informações: ")
print(f"Numérico: {info.isnumeric()}")
print(f"Alpha numérico: {info.isalnum()}")
print(f"Contém no alfabeto: {info.isalpha()}")