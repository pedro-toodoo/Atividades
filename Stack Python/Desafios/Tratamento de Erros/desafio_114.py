import urllib.error
import requests

try:
    r = requests.head("http://pudim.com.br/")
except urllib.error.URLError:
    print("Não há conexão com a internet!")
except Exception as erro:
    print(f"ERRO... Problema: {erro.__class__}")
else:
    print("O site está up!")
