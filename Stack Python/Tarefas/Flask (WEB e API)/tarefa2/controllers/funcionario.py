from tarefa2.models.models import db, Funcionario
from flask import Blueprint, Response, request
import json

tarefa2 = Blueprint("Funcionario", __name__)

@tarefa2.route('/')
def index():
    #funcionario = Funcionario.query.all()
    #result = [e.to_dict() for e in funcionario]
    rows = db.session.execute("select * from funcionario").fetchall()
    result = [dict(r) for r in rows]
    return Response(response=json.dumps(result), status=200, content_type="application/json")

@tarefa2.route('/<int:id>/dependentes')
def dependentes(id):
    rows = db.session.execute("select F.nome, D.nome from funcionario F JOIN dependente D ON D.Funcionario_id = F.id where F.id = %s" % id)
    result = [dict(r) for r in rows]
    return Response(response=json.dumps(result), status=200, content_type="application/json")

@tarefa2.route('/view/<int:id>', methods=['GET'])
def view(id):
    row = db.session.execute("select * from funcionario where id = %s" % id).fetchone()
    return Response(response=json.dumps(dict(row)), status=200, content_type="application/json")


@tarefa2.route('/add', methods=['POST'])
def add():
    funcionario = Funcionario(request.form['nome'], request.form['endereco'])
    db.session.add(funcionario)
    db.session.commit()
    return Response(response=json.dumps({'status': 'success', 'data': funcionario.to_dict()}), status=200, content_type="application/json")

@tarefa2.route('/edit/<int:id>', methods=['PUT', 'POST'])
def edit(id):
    funcionario = Funcionario.query.get(id)
    funcionario.nome = request.form['nome']
    funcionario.endereco = request.form['endereco']
    db.session.commit()
    return Response(response=json.dumps(funcionario.to_dict()), status=200, content_type="application/json")

@tarefa2.route('/delete/<int:id>', methods=['GET', 'DELETE'])
def delete(id):
    funcionario = Funcionario.query.get(id)
    db.session.delete(funcionario)
    db.session.commit()
    return Response(response=json.dumps(funcionario.to_dict()), status=200, content_type="application/json")