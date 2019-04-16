import os
from flask import Flask, render_template, request
from run_model import run_model
from model import retrain_model

def display():
    return render_template("upload_retrain.html")

def upload():
    files = []
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(APP_ROOT, 'data/')

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        filename = file.filename
        destination = "/".join([target, filename])
        file.save(destination)
        files.append(filename)

    #retrain model with the file we just got
    retrain_model(files)
    
    return render_template("complete_retrain.html")
