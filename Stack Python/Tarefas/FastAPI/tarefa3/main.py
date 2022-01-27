import requests
from interface import *
import json

#url = "http://localhost:8000/produtos"
#requisicao = requests.get(url)

#print(requisicao.json())

while True:
    resp = menu(['Cadastrar usuário', 'Fazer login', 'Listar produtos', 'Buscar produto por ID', 'Buscar produto pelo nome'])

    if resp == 1:
        username = input("Nome de usuário: ")
        password = input("Senha: ")
        endereco = input("Endereço: ")
        conta = input("Conta bancária: ")

        novo_usuario = {
            "usuario": username,
            "senha": password,
            "endereco": endereco,
            "conta_bancaria": conta
        }

        url = "http://localhost:8000/add_usuario/"
        requisicao = requests.post(url, data=json.dumps(novo_usuario))
        print(requisicao.text)

    if resp == 2:
        username = input("Nome de usuário: ")
        password = input("Senha: ")
        url = "http://localhost:8000/token"
        requisicao = requests.post(url, data={"username": username, "password": password})
        print(requisicao.text)


    elif resp == 3:
        url = "http://localhost:8000/produtos"
        requisicao = requests.get(url)
        dados = requisicao.json()
        for i in dados['produtos']:
            cabecalho(i['nome'])
            print(f"Preço: R${i['preco']}")
            print(f"Descrição: {i['descricao']}")

    elif resp == 4:
        prod_id = int(input("Informe o ID do produto: "))
        url = f"http://localhost:8000/produto/{prod_id}"
        requisicao = requests.get(url)
        dados = requisicao.json()
        print(f"Nome do produto: {dados['nome']}")
        print(f"Preço do produto: R${dados['preco']}")
        print(f"Descrição do produto: {dados['descricao']}")

    elif resp == 5:
        nome = input("Informe o nome do produto: ")
        url = f"http://localhost:8000/pesquisa_produto?nome={nome}"
        requisicao = requests.get(url)
        dados = requisicao.json()
        for i in dados['produtos']:
            cabecalho(i['nome'])
            print(f"Preço: R${i['preco']}")
            print(f"Descrição: {i['descricao']}")
