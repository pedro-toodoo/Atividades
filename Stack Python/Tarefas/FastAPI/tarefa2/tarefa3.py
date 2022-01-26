import requests


url = "http://localhost:8000/produtos"
requisicao = requests.get(url)

print(requisicao.json())