from mongoengine import Document, StringField, FloatField, IntField, DictField


class Produto(Document):
    prod_id = IntField()
    nome = StringField(max_length=100)
    preco = FloatField()
    descricao = StringField(max_length=100)

class Usuario(Document):
    usuario = StringField(max_length=100)
    senha = StringField(max_length=100)
    endereco = StringField(max_length=100)
    conta_bancaria = StringField(max_length=100)