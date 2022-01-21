import ormar
from config import database, metadata


class Produto(ormar.Model):
    class Meta: #criar modelo e conectar com o banco
        metadata = metadata
        database = database
        tablename ="produto"

    id: int = ormar.Integer(primary_key=True)
    titulo: str = ormar.String(max_length=100)
    descricao: str = ormar.String(max_length=11)
    valor: float = ormar.Integer()

