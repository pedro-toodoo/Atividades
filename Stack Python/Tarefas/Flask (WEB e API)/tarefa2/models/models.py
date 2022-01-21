from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Funcionario(db.Model):
    __tablename__ = 'funcionario'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    endereco = db.Column(db.String(150))
    #dependentes = db.relationship('Dependente', backref='funcionario')

    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        #self.dependentes = dependentes

    def to_dict(self, columns=[]):
        if not columns:
            return {"id": self.id, "nome": self.nome, "endereco": self.endereco}
        else:
            return {col: getattr(self, col) for col in columns} #getattr pega atributo de uma classe (estudante)

class Dependente(db.Model):
    __tablename__ = 'dependente'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    endereco = db.Column(db.String(150))
    Funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionario.id'))

    def __init__(self, nome, endereco, Funcionario_id):
        self.nome = nome
        self.endereco = endereco
        self.Funcionario_id = Funcionario_id

    def to_dict(self, columns=[]):
        if not columns:
            return {"id": self.id, "nome": self.nome, "endereco": self.endereco, "Funcionario_id": self.Funcionario_id}
        else:
            return {col: getattr(self, col) for col in columns} #getattr pega atributo de uma classe (estudante)
