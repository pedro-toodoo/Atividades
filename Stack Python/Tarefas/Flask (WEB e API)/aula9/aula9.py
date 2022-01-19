from flask import Flask, render_template, request

aula9 = Flask(__name__, template_folder='templates')

@aula9.route('/')
def index():
    x = 50
    y = 25
    query = request.args.to_dict()
    return render_template('modelo.html', x=x, y=y, query=query)

if __name__ == '__main__':
    aula9.run(debug=True)