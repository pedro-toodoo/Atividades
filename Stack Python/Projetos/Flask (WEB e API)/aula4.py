from flask import Flask, redirect, url_for

aula4 = Flask(__name__)

aula4.add_url_rule('/', 'index')

@aula4.route('/admin')
def admin():
    return '<h1>Teste aqui administrador</hr>'

@aula4.route('/guest/<guest>')
def guest(guest):
    return f'<h1>Olá convidado {guest}</h1>'

@aula4.route('/user/<name>')
def user(name):
    if name ==  'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', guest=name))

@aula4.route('/google')
def google():
    return redirect('http://www.google.com.br')

if __name__ == '__main__':
    aula4.run(debug=True)