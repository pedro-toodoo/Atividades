vel = float(input("Qual a velocidade do carro? "))

if vel > 80:
    print("Você foi multado!")
    print(f"A multa será no valor de R${(vel - 80)*7}")
else:
    print("Ok! Limite de velocidade permitido!")