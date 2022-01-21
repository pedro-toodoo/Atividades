import sqlalchemy
from config import DATABASE_URL, metadata
from models.usuario import Usuario
from models.produto import Produto

def config_db(database_url=DATABASE_URL):
    engine = sqlalchemy.create_engine(database_url)
    metadata.drop_all(engine)
    metadata.create_all(engine)

if __name__ == '__main__':
    config_db()