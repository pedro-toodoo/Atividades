from flask import Blueprint, Response, request
import json
from aula16.models.models import db, Estudante


from flask import Blueprint, Response, request
import json
from aula16.models.models import db, Estudante

aula16 = Blueprint("Estudante", __name__)

@aula16.route('/')
def index():
    estudantes = Estudante.query.all()
    result = [e.to_dict() for e in estudantes]
    #return render_template('index.html', estudantes=estudantes)
    rows = db.session.execute("select * from estudante").fetchall()
    result1 = [dict(r) for r in rows]
    return Response(response=json.dumps(result), status=200, content_type="application/json")

@aula16.route('/view/<int:id>', methods=['GET'])
def view(id):
    row = db.session.execute("select * from estudante where id = %s" % id).fetchone()
    return Response(response=json.dumps(dict(row)), status=200, content_type="application/json")


@aula16.route('/add', methods=['POST'])
def add():
    estudante = Estudante(request.form['nome'], request.form['idade'])
    db.session.add(estudante)
    db.session.commit()
    return Response(response=json.dumps({'status': 'success', 'data': estudante.to_dict()}), status=200, content_type="application/json")

@aula16.route('/edit/<int:id>', methods=['PUT', 'POST'])
def edit(id):
    estudante = Estudante.query.get(id)
    #if request.method == 'POST':
    estudante.nome = request.form['nome']
    estudante.idade = request.form['idade']
    db.session.commit()
    return Response(response=json.dumps(estudante.to_dict()), status=200, content_type="application/json")
    #return redirect(url_for('index'))
#return render_template('edit.html', estudante=estudante)

@aula16.route('/delete/<int:id>', methods=['GET', 'DELETE'])
def delete(id):
    estudante = Estudante.query.get(id)
    db.session.delete(estudante)
    db.session.commit()
    return Response(response=json.dumps(estudante.to_dict()), status=200, content_type="application/json")