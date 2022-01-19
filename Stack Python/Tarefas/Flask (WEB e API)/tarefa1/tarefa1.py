from flask import Flask, render_template, session, request, redirect, url_for, make_response

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('login'))

@app.route('/setcookie', methods=['GET', 'POST'])
def setcookie():
    if request.method == 'POST':
        if request.form['username'] == 'pedro' and request.form['password'] == '123':
            resp = make_response(render_template('validado.html'))
            username = request.form['username']
            password = request.form['password']
            resp.set_cookie('username', username)
            resp.set_cookie('password', password)
        else:
            resp = make_response(render_template('erro.html'))
    return resp

@app.route('/getcookie')
def getcookie():
    user = request.cookies.get('username')
    password = request.cookies.get('password')
    return f'Valor do cookie: <br>Usuário: {user}<br>Senha: {password}'


if __name__ == '__main__':
    app.run(debug=True)