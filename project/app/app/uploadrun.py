import os
from flask import Flask, render_template, request
from run_model import run_model

def display():
    return render_template("upload.html")

def upload():
    results = []
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(APP_ROOT, 'data/')

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        filename = file.filename
        destination = "/".join([target, filename])
        file.save(destination)
        results.append(run_model(destination))

    s_count = 0
    for i in results:
        for j in i:
            if(j == 1):
                s_count+=1
        
    f_result = open("./templates/complete.html", "w")
    f_result.write("")
    f_result.close
    f_result = open("./templates/complete.html", "a")
    f_result.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<meta charset=\"UTF-8\">\n\t<title>Title</title>\n</head>\n<body>")
    f_result.write("S-Cone Count = " + str(s_count))
    f_result.write("\n</body>\n</html>")
    f_result.close()
    
    return render_template("complete.html")
