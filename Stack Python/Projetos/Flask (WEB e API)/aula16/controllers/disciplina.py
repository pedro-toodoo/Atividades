from flask import Blueprint, Response, request
import json
from tarefa2.models.models import db, Dependente

aula16 = Blueprint("Disciplina", __name__)

@aula16.route('/')
def index():
    disciplina = Disciplina.query.all()
    result = [e.to_dict() for e in disciplina]
    return Response(response=json.dumps(result), status=200, content_type="application/json")

@aula16.route('/view/<int:id>', methods=['GET'])
def view(id):
    row = db.session.execute("select * from disciplina where id = %s" % id).fetchone()
    return Response(response=json.dumps(dict(row)), status=200, content_type="application/json")


@aula16.route('/add', methods=['POST'])
def add():
    disciplina= Disciplina(request.form['nome'])
    db.session.add(disciplina)
    db.session.commit()
    return Response(response=json.dumps({'status': 'success', 'data': disciplina.to_dict()}), status=200, content_type="application/json")

@aula16.route('/edit/<int:id>', methods=['PUT', 'POST'])
def edit(id):
    disciplina= Disciplina.query.get(id)
    disciplina.nome = request.form['nome']
    db.session.commit()
    return Response(response=json.dumps(disciplina.to_dict()), status=200, content_type="application/json")

@aula16.route('/delete/<int:id>', methods=['GET', 'DELETE'])
def delete(id):
    disciplina= Disciplina.query.get(id)
    db.session.delete(disciplina)
    db.session.commit()
    return Response(response=json.dumps(disciplina.to_dict()), status=200, content_type="application/json")