from flask import Flask
from models.models import db
from controllers.funcionario import tarefa2 as funcionario_controller
from controllers.dependente import tarefa2 as dependente_controller

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///empresa.sqlite3'

app.register_blueprint(funcionario_controller, url_prefix="/funcionario/")
app.register_blueprint(dependente_controller, url_prefix="/dependente/")

if __name__ == '__main__':
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run(debug=True)