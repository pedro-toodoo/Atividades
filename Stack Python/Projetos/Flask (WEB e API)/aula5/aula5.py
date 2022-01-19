from flask import Flask

aula5 = Flask(__name__, static_folder='public')


if __name__ == '__main__':
    aula5.run(debug=True)