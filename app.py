from flask import Flask, render_template, request, redirect, url_for, flash
import DemoMain
import os
import DemoRealTime
from werkzeug.utils import secure_filename


app = Flask(__name__)
UPLOAD_FOLDER = 'C:\\Users\\Admin\\PycharmProjects\\TalkingHead_FinalYear\\rawFile'
ALLOWED_EXTENSIONS = set(['raw'])


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/play')
def hello():
    DemoMain.run()
    return render_template('index.html')


@app.route('/form')
def form():
    return render_template('uploadFormTest.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename('raw_file.raw')
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file',
                                    filename=filename))
    return render_template('index.html')


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run()


