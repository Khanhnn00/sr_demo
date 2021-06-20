import os, glob
from flask import Flask, request, redirect, render_template, flash
from werkzeug.utils import secure_filename
from test import main
# from srrescgan.predict import main_srrescgan
import numpy as np
import time

UPLOAD_FOLDER = 'static/uploads/'
DOWNLOAD_FOLDER = 'static/downloads/'
ALLOWED_EXTENSIONS = {'jpg', 'png', '.jpeg'}
app = Flask(__name__, static_url_path="/static")

# APP CONFIGURATIONS
app.config['SECRET_KEY'] = 'opencv'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
# limit upload size upto 6mb
app.config['MAX_CONTENT_LENGTH'] = 6 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file attached in request')
            return redirect(request.url)
        file = request.files['file']
        model = request.form.get('comp_select')
        print(model)
        # printadaadada
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            ul = glob.glob('./static/downloads/*')
            for f in ul:
                os.remove(f)
            ul = glob.glob('./static/uploads/*')
            for f in ul:
                os.remove(f)
            filename = secure_filename(file.filename)
            file.save(os.path.join(DOWNLOAD_FOLDER, filename))
            process_file(os.path.join(DOWNLOAD_FOLDER, filename), filename, model)

            data = {
                "output_img": 'static/uploads/' + 'output.png',
                "input_img": 'static/downloads/' + filename
            }
            return render_template("index.html", data=data)
    return render_template('index.html')


def process_file(path, filename, model):
    main(model)
    # elif model == 'SRResCGAN':
    #     main_srrescgan()


if __name__ == '__main__':
    app.run(debug=True)
