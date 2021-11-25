from random import shuffle

nome = input(f"Digite o nome de um aluno: ")
nome2 = input(f"Digite o nome de outro aluno: ")
nome3 = input(f"Digite o nome de outro aluno: ")
nome4 = input(f"Digite o nome de outro aluno: ")

l = [nome, nome2, nome3, nome4]
shuffle(l) #embaralhando a lista acima

print(f"Ordem de apresentação: {l}")