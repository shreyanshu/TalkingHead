from flask import Flask, render_template, request, redirect, url_for, flash
import DemoMain
import os
import DemoRealTime
from werkzeug.utils import secure_filename
import matplotlib.pyplot as plt
import RawToPhoneme


app = Flask(__name__)
UPLOAD_FOLDER = 'C:\\Users\\Admin\\PycharmProjects\\TalkingHead_FinalYear\\rawFile'
ALLOWED_EXTENSIONS = set(['raw'])


@app.route('/')
def hello_world():
    return render_template('index.html')


# @app.route('/form')
# def form():
#     render_template('selectFace.html')


@app.route('/form')
def form():
    return render_template('uploadFormTest.html')


@app.route('/realtimeform')
def realTimeForm():
    # if request.method == 'POST':
    return render_template('RealTimeForm.html')


@app.route('/breakPhonemes')
def breakPhoneme():
    # if request.method == 'POST':
    return render_template('breakPhoneme.html')


@app.route('/splitPhonemes', methods=['GET', 'POST'])
def splitPhoneme():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            # return redirect(request.url)
        file = request.files['file']

        result = request.form

        # print(result['mouth'])

        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename('raw_file.raw')
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            phonemeList = RawToPhoneme.phonemes()

        return render_template('breakPhoneme.html', phonemeList=phonemeList)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            # return redirect(request.url)
        file = request.files['file']

        result = request.form

        # print(result['mouth'])

        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename('raw_file.raw')
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            DemoMain.run(result['mouth'])
            return redirect(url_for('upload_file',
                                    filename=filename))


    return render_template('index.html')


@app.route('/realtime',  methods=['GET', 'POST'])
def realtime():
    if request.method == 'POST':
        result = request.form
        DemoRealTime.run(result['mouth'])
        plt.close('all')
    return render_template('RealTimeForm.html')


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run()


