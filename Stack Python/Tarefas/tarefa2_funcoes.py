from datetime import datetime

#meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

def data(d):
    #aux = input("Informe uma data (DD/MM/AAAA): ")
    #if d[2] == "/" and d[5] == "/":
    try:
        datetime.strptime(d, "%d/%m/%Y")
    except ValueError:
        print("ERRO. Data no formato errado!")
        return None
    else:
        string_data = datetime.strptime(d, "%d/%m/%Y")
        return datetime.strftime(string_data, "%d de %B de %Y") #d = dia / B = mes extenso / Y = com 4 dígitos

extenso = input("Informe uma data (DD/MM/AAAA): ")

resp = data(extenso)

if resp != None:
    print(resp)