n = int(input("Informe um número: "))

soma = 0
for i in range(0, n):
    idade = int(input("Idade: "))
    soma += idade

media = soma / n

if media > 0 and media <= 25:
    print("Turma é JOVEM!")
elif media > 25 and media <= 60:
    print("Turma é ADULTA!")
elif media > 60:
    print("Turma é IDOSA!")