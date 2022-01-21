from flask import Blueprint, Response, request
import json
from tarefa2.models.models import db, Dependente

tarefa2 = Blueprint("Dependente", __name__)

@tarefa2.route('/')
def index():
    rows = db.session.execute("select * from dependente").fetchall()
    result = [dict(r) for r in rows]
    return Response(response=json.dumps(result), status=200, content_type="application/json")

@tarefa2.route('/view/<int:id>', methods=['GET'])
def view(id):
    row = db.session.execute("select * from dependente where id = %s" % id).fetchone()
    return Response(response=json.dumps(dict(row)), status=200, content_type="application/json")


@tarefa2.route('/add', methods=['POST'])
def add():
    dependente= Dependente(request.form['nome'], request.form['endereco'], request.form['Funcionario_id'])
    db.session.add(dependente)
    db.session.commit()
    return Response(response=json.dumps({'status': 'success', 'data': dependente.to_dict()}), status=200, content_type="application/json")

@tarefa2.route('/edit/<int:id>', methods=['PUT', 'POST'])
def edit(id):
    dependente = Dependente.query.get(id)
    dependente.nome = request.form['nome']
    dependente.endereco = request.form['endereco']
    dependente.Funcionario_id = request.form['Funcionario_id']
    db.session.commit()
    return Response(response=json.dumps(dependente.to_dict()), status=200, content_type="application/json")

@tarefa2.route('/delete/<int:id>', methods=['GET', 'DELETE'])
def delete(id):
    dependente = Dependente.query.get(id)
    db.session.delete(dependente)
    db.session.commit()
    return Response(response=json.dumps(dependente.to_dict()), status=200, content_type="application/json")