from flask import Flask, render_template, request, send_file
import os
from werkzeug.utils import secure_filename

aula13 = Flask(__name__, template_folder='templates')
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload')

@aula13.route('/')
def index():
    return render_template('index.html')

@aula13.route('/upload', methods=['POST'])
def upload():
    file = request.files['imagem']
    savePath = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(savePath)
    return 'Upload feito com sucesso'

@aula13.route('/get-file/<filename>')
def getFile(filename): #para fazer o download da imagem contida na pasta upload
    file = os.path.join(UPLOAD_FOLDER, filename + '.jpg')
    return send_file(file, mimetype='imagem/jpg')

if __name__ == '__main__':
    aula13.run(debug=True)

