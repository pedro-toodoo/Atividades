from random import choice

nome = input(f"Digite o nome de um aluno: ")
nome2 = input(f"Digite o nome de outro aluno: ")
nome3 = input(f"Digite o nome de outro aluno: ")
nome4 = input(f"Digite o nome de outro aluno: ")

l = [nome, nome2, nome3, nome4]

print(f"O aluno(a) sorteado(a) para apagar o quadro é {choice(l)}")