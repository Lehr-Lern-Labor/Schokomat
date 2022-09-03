import os
from flask import Flask, flash, request, redirect, url_for, get_flashed_messages, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'json', 'py'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename:str) -> bool:
    extension = filename.rsplit('.', 1)[-1].lower()
    return extension in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the 'file' was uploaded
        if 'uploaded_file' not in request.files:
            return 'Es wurde keine Datei hochgeladen.'
        file = request.files['uploaded_file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if not file or file.filename == '':
            return 'Es wurde keine Datei ausgewählt.'
        if not allowed_file(file.filename):
            return 'Falscher Dateityp.'
        filename = "automat.json" #secure_filename(file.filename)
        filedata = file.read().decode("utf-8")
        with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), "w", encoding="utf-8") as outfile:
            outfile.write(filedata)
        return 'Die Datei: ' + file.filename + ' wurde gespeichert!'

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=uploaded_file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/get_your_file_here/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

app.run(debug=True, host='0.0.0.0')