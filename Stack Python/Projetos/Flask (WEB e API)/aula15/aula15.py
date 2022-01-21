import json

from flask import Flask, render_template, request, redirect, url_for, Response
from models import db, Estudante

aula15 = Flask(__name__, template_folder='templates')
aula15.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudantes.sqlite3'

@aula15.route('/')
def index():
    estudantes = Estudante.query.all()
    result = [e.to_dict() for e in estudantes]
    #return render_template('index.html', estudantes=estudantes)
    rows = db.session.execute("select * from estudante").fetchall()
    result1 = [dict(r) for r in rows]
    return Response(response=json.dumps(result), status=200, content_type="application/json")

@aula15.route('/view/<int:id>', methods=['GET'])
def view(id):
    row = db.session.execute("select * from estudante where id = %s" % id).fetchone()
    return Response(response=json.dumps(dict(row)), status=200, content_type="application/json")


@aula15.route('/add', methods=['POST'])
def add():
    estudante = Estudante(request.form['nome'], request.form['idade'])
    db.session.add(estudante)
    db.session.commit()
    return aula15.response_class(response=json.dumps({'status': 'success', 'data': estudante.to_dict()}), status=200, content_type="application/json")

@aula15.route('/edit/<int:id>', methods=['PUT', 'POST'])
def edit(id):
    estudante = Estudante.query.get(id)
    #if request.method == 'POST':
    estudante.nome = request.form['nome']
    estudante.idade = request.form['idade']
    db.session.commit()
    return Response(response=json.dumps(estudante.to_dict()), status=200, content_type="application/jsonnt")
    #return redirect(url_for('index'))
#return render_template('edit.html', estudante=estudante)

@aula15.route('/delete/<int:id>', methods=['GET', 'DELETE'])
def delete(id):
    estudante = Estudante.query.get(id)
    db.session.delete(estudante)
    db.session.commit()
    return Response(response=json.dumps(estudante.to_dict()), status=200, content_type="application/jsonnt")

if __name__ == '__main__':
    db.init_app(app=aula15)
    with aula15.test_request_context():
        db.create_all()
    aula15.run(debug=True)