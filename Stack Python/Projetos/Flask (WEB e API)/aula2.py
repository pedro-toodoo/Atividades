from flask import Flask

aula2 = Flask(__name__)

@aula2.route('/')
def index():
    #d = 3 / 0
    return 'teste atualização página'

def teste():
    return '<p> Testando 1</p>'

def teste2():
    return '<p> Testando 2</p>'
aula2.add_url_rule('/teste', 'teste', teste)
aula2.add_url_rule('/teste-2', 'teste-2', teste2)

if __name__ == '__main__':
    aula2.run(debug=True, port=3000)