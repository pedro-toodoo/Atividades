from flask import Flask, request
from json import dumps

aula6 = Flask(__name__, static_folder='public')


@aula6.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        #return f"OK MEU TRUTA POST resultado: {request.form['nome']}"
        return dumps(request.form)
    return "Ok MEU TRUTA GET"

if __name__ == '__main__':
    aula6.run(debug=True)