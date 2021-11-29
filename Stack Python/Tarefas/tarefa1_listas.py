lista = []
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
soma = 0

for i in range(0, 12):
    lista.append(float(input("Digite a temperatura média: ")))
    soma += lista[i]

media = soma / len(lista)

for i in range(0, 12):
    if lista[i] > media:
        print(f"Mês: {meses[i]} - Temperatura: {lista[i]}ºC")