pessoas = {"nome": "Pedro", "sexo": "M", "idade": 23 }
print(f"{pessoas['nome']} tem {pessoas['idade']} anos! ")

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items()) #conjunto de tuplas
del pessoas['sexo']
pessoas['peso'] = 68
for k, v in pessoas.items():
    print(f"{k} = {v}")

brasil = []
estado1 = {"uf": "Rio de Janeiro", "sigla": "RJ"}
estado2 = {"uf": "São Paulo", "sigla": "SP"}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[1]['uf'])

estado = {}
brasil = []

for i in range(0, 3):
    estado['uf'] = input("UF: ")
    estado['sigla'] = input("Sigla: ")
    brasil.append(estado.copy())
print(brasil)