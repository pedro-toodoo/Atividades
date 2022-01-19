from flask import Flask, render_template, request, make_response

aula11 = Flask(__name__, template_folder='templates')

@aula11.route('/')
def index():
    return render_template('index.html')

@aula11.route('/setcookie', methods=['GET', 'POST'])
def setcookie():
    resp = make_response(render_template('setcookie.html'))
    if request.method == 'POST':
        dados = request.form['c']
        resp.set_cookie('testeCookie', dados)
    return resp

@aula11.route('/getcookie')
def getcookie():
    cookieName = request.cookies.get('testeCookie')
    return f'Valor do cookie: {cookieName}'


if __name__ == '__main__':
    aula11.run(debug=True)

