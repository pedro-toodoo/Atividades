from flask import Flask, render_template, session, request, redirect, url_for

aula12 = Flask(__name__, template_folder='templates')
aula12.secret_key = "123"

@aula12.route('/')
def index():
    username = ''
    if 'username' in session:
        username = session['username']
    return render_template('validado.html', username=username)

@aula12.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and request.form['username'] != '':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')

@aula12.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    aula12.run(debug=True)