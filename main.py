import os
from flask import Flask, request, redirect, url_for, render_template, flash ,abort
import json
import boto3
import settings
import secrets 

region = "ap-northeast-1"

s3 = boto3.client('s3', aws_access_key_id=settings.accesskey, aws_secret_access_key= settings.secretkey, region_name=region)

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg' ])

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('ファイルがありません')
        return "not file"

    file = request.files['file']
    save_name = request.form["save_name"]

    if file.filename == '':
        flash('ファイルがありません')
        return "not file"
    if file and allowed_file(file.filename):
        filename = secrets.token_urlsafe(12)+".png"
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        s3.upload_file(filepath,settings.bucket_name, save_name )
        os.remove( filepath )
        return "ok"


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host ='0.0.0.0',port = port)