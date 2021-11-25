cpf = input("Digite seu CPF no formato (XXX.XXX.XXX-XX): ")

if cpf[3] == "." and cpf[7] == "." and cpf[11] == "-" and len(cpf) == 14:
    print("CPF válido!")
else:
    print("CPF não está no formato desejado!")

