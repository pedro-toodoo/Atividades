from flask import Flask, request, abort, redirect, url_for

aula8 = Flask(__name__)

@aula8.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['passw'] == 'admin':
            return redirect(url_for('sucesso'), code=302)
        else:
            abort(401)
    else:
        abort(403) #proibído

@aula8.route('/sucesso')
def sucesso():
    return "Login feito com sucesso"



if __name__ == '__main__':
    aula8.run(debug=True)