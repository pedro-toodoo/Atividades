nome = input("Digite seu nome completo:")

print(f"Nome com todas as letras maiúsculas: {nome.upper()}")
print(f"Nome com todas as letras minúsculas: {nome.lower()}")

espacos = nome.count(" ")
print(espacos)
print(f"total de letras: {len(nome) - espacos}")

primeiro = nome.split()
print(primeiro)
print(f"Quantas letras tem o primeiro nome: {len(primeiro[0])}")
