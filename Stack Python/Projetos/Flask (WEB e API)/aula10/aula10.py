from flask import Flask, render_template, request

aula10 = Flask(__name__, template_folder='templates')

@aula10.route('/')
def notas():
    return render_template('notas.html')

@aula10.route('/result', methods=['POST'])
def resultado():
    total = sum([int(v) for v in request.form.to_dict().values()])
    return render_template('calculo.html', total = total)

if __name__ == '__main__':
    aula10.run(debug=True)

