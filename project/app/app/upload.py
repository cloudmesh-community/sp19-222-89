import os
from flask import Flask, render_template, request

def display():
    return render_template("upload.html")

def upload():
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(APP_ROOT, 'data/')

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        filename = file.filename
        destination = "/".join([target, filename])
        file.save(destination)

    return render_template("complete.html")

"""post:
      operationId: upload.upload
      description: "Allows user to upload file"
      produces:
        - "text/html"
      parameters:
        - name: file
          in: body
          description: File to upload
          required: True
          
      responses:
        "201":
          description: "File upload successful"""


"""/:
    get:
      operationId: index.display
      description: "Returns index html page"
      responses:
        "200":
          description: "Displayed successfully"""
