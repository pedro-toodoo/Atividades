from typing import Optional #parâmetro não é obrigatório

from fastapi import FastAPI, Header, Response, Cookie

from pydantic import BaseModel

class Item(BaseModel):
    id: int
    quantidade: int
    descricao: str
    valor: float

app = FastAPI()


db = []

@app.post('/item')
def add_item(item: Item):
    db.append(item)
    return item

@app.get('/listagem')
def lista_items():
    return db

@app.get('/item/valortotal')
def get_valor_total():
    #total = 0
    #for i in db:
        #total += i.valor * i.quantidade
    total = sum(i.valor * i.quantidade for i in db)
    return {"valor_total": total}

