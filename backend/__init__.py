
from flask import *
from flask_autoindex import AutoIndex
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = "/home/<hmmm>"
# pls change this, thanks!
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)
AutoIndex(app, browse_root=UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    x = request.args.get('path')
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            if x != None:
                path = app.config['UPLOAD_FOLDER'] + x
                file.save(os.path.join(path, filename))
            else:
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('/')

    return '''  
    <!doctype html>
    <title>Upload  a new File</title>
    <h1>Upload a new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
