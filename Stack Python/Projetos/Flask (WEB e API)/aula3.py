from flask import Flask

aula3 = Flask(__name__)

@aula3.route('/hello/')
@aula3.route('/hello/<nome>')
def hello(nome=""):
    return f'<h1>Hello World! {nome}</h1>'

@aula3.route('/blog/')
@aula3.route('/blog/<int:postID>')
def blog(postID=-1):
    if postID >= 0:
        return f'blog info {postID}'
    else:
        return 'blog todo'


if __name__ == '__main__':
    aula3.run(debug=True)