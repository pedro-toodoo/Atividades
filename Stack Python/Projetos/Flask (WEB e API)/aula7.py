import json

from flask import Flask, request

aula7 = Flask(__name__)

@aula7.route('/', methods=['GET', 'POST'])
def index():
    #print(request.method, request.args)
    t1 = request.args.to_dict()
    t2 = dict(request.args)

    return json.dumps([t1, t2])


if __name__ == '__main__':
    aula7.run(debug=True)