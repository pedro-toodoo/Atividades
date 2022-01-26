from fastapi import FastAPI, Path, Query, Body, Depends, HTTPException
from mongoengine.queryset.visitor import Q
from pydantic import BaseModel

from models import Produto, Usuario
from mongoengine import connect #conectar com mongoDB
import json #deixar em formato de dicionário (json)
from passlib.context import CryptContext #hash da senha
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta, datetime
from jose import jwt
from secrets import token_hex

app = FastAPI()
connect(db="loja", host="localhost", port=27017)


@app.get('/produtos')
def get_produtos():
    produtos = json.loads(Produto.objects().to_json()) #retorna todos os produtos no formato json

    return {"produtos": produtos}

@app.get('/produto/{prod_id}')
def get_produto_id(prod_id: int = Path(..., gt=0)):
    produto = Produto.objects.get(prod_id=prod_id)

    produto_dict = {
        "prod_id": produto.prod_id,
        "nome": produto.nome,
        "preco": produto.preco,
        "descricao": produto.descricao
    }

    return produto_dict

@app.get('/pesquisa_produto')
def pesquisa_produto(nome, preco: float = Query(None, gt=0)):
    produtos = json.loads(Produto.objects.filter(Q(nome__icontains=nome) | Q(preco=preco)).to_json()) #verifica se o que foi digitado está contido em algum nome

    return {"produtos": produtos}

class NovoProduto(BaseModel): #estrutura para criação de produto
    prod_id: int = Body(None, gt=0)
    nome: str
    preco: float = Body(None, gt=0)
    descricao: str

@app.post('/add_produto')
def add_produto(produto: NovoProduto):
    novo_prod = Produto(prod_id=produto.prod_id,
                        nome=produto.nome,
                        preco=produto.preco,
                        descricao=produto.descricao
                        )
    novo_prod.save()

    return "Produto cadastrado com sucesso! :)"

#usuário
@app.get('/usuarios')
def get_usuarios():
    usuarios = json.loads(Usuario.objects().to_json())

    return {"usuarios": usuarios}

class NovoUsuario(BaseModel): #estrutura para criação de produto
    usuario: str
    senha: str
    endereco: str
    conta_bancaria: str


senha_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def get_senha_hash(senha):
    return senha_context.hash(senha)

@app.post('/add_usuario')
def add_usuario(usu: NovoUsuario):
    novo_usuario = Usuario(usuario=usu.usuario,
                        senha=get_senha_hash(usu.senha),
                        endereco=usu.endereco,
                        conta_bancaria=usu.conta_bancaria
                        )
    novo_usuario.save()

    return "Usuário cadastrado com sucesso! :)"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def autenticar_usuario(username, password):
    try:
        username = json.loads(Usuario.objects.get(usuario=username).to_json())
        senha_check = senha_context.verify(password, username['senha'])
        return senha_check
    except Usuario.DoesNotExist:
        return False

def cria_token_acesso(data: dict, expires_delta: timedelta):
    SECRET_KEY = token_hex(32)
    ALGORITHM = "HS256"
    to_enconde = data.copy()

    expire = datetime.now() + expires_delta #expira depois de 60min

    to_enconde.update(({"exp": expire}))

    encoded_jwt = jwt.encode(to_enconde, SECRET_KEY, algorithm=ALGORITHM)

    #print(SECRET_KEY)

    return encoded_jwt


@app.post('/token')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password

    if autenticar_usuario(username, password):
        access_token = cria_token_acesso(data={"sub": username}, expires_delta=timedelta(minutes=60))
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=400, detail="Usuário ou senha incorretos")


@app.get('/')
def home(token: str = Depends(oauth2_scheme)):
    return {"token": token}
