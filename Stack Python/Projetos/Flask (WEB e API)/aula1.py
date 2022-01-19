from flask import Flask

aula1 = Flask(__name__)


@aula1.route("/")
def index():
    return 'index'


@aula1.route("/api/v2")
def indexv2():
    return 'Segunda versão'


if __name__ == '__main__':
    aula1.run()
