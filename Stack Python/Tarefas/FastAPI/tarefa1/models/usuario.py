import ormar
from config import database, metadata


class Usuario(ormar.Model):
    class Meta: #criar modelo e conectar com o banco
        metadata = metadata
        database = database
        tablename ="usuario"

    id: int = ormar.Integer(primary_key=True)
    nome: str = ormar.String(max_length=100)
    cpf: str = ormar.String(max_length=11)
    pagamento: str = ormar.String(max_length=10)

