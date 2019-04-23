import os
from flask import Flask, render_template, request
import scripts
from scripts.run_model import run_model

def display():
    return render_template("upload.html")

def upload():
    results = []
    input_data = []
    s_cone_indices = {}
    s_count  = 0
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(APP_ROOT, '../data/')

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        filename = file.filename
        destination = "/".join([target, filename])
        file.save(destination)
        answer, input_formatted = run_model(destination)
        results.append(answer)
        input_data.append(input_formatted)

        s_cone_indices[file.filename] = []

        for i in range(len(answer)):
            if(answer[i]==1):
                s_count +=1
                s_cone_indices[file.filename].append(i)
                    
    #Get metrics of current model from ./model_files/metrics.txt
    with open("./model_files/metrics.txt") as flist:
        lines = flist.readlines()

    f_result = open("./templates/complete.html", "w")
    f_result.write("")
    f_result.close
    f_result = open("./templates/complete.html", "a")
    f_result.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<meta charset=\"UTF-8\">\n\t<title>Title</title>\n</head>\n<body>")
    f_result.write("S-Cone Count = " + str(s_count) + "<br /><br /><br />")
    
    for item in s_cone_indices:
        #current array index in our input_data list of arrays
        ind = 0

        #Each file has its own array of lists. So we have a list of
        #arrays of lists

        #Get one array
        curr_array = input_data[ind]

        #Iterate through each list in that array
        #If the index of that list is listed as a 1 in the
        #corresponding list in results, then write a table

        #table_count helps me with making the title of each new table
        #the file name and not doing that a bunch of times
        table_count = 0
        for i in range(len(curr_array)):
            #Checks for the if described in the above comment
            
            
            if(results[ind][i] == 1):
                if(table_count == 0):
                    f_result.write(
                        '<style type="text/css">'
                        '.tg  {border-collapse:collapse;border-spacing:0;}'
                        '.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}'
                        '.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}'
                        '.tg .tg-s268{text-align:left}'
                        '</style>'
                        '<table class="tg">'
                        '<tr>'
                        '<th class="tg-xldj" colspan="3">' +  str(item) + '</th>'
                        '</tr>')
                    table_count += 1

                f_result.write(
                '<tr>'
                '<th class="tg-s268">'+ str(i) +'</th>'
                '<th class="tg-s268">'+ str(curr_array[i][0]) + '</th>'
                '<th class="tg-s268">'+ str(curr_array[i][1]) + '</th>'
                '<th class="tg-s268">'+ str(curr_array[i][2]) + '</th>'
                '</tr>')
        f_result.write('</table>')
        table_count = 0
        ind += 1
    
    #write model information to bottom
    f_result.write("<br /><br /><br /><br /><br /><br />")
    f_result.write("Current model is Deep Neural Network<br/>")
    f_result.write("Current model made: " + str(lines[0].rstrip()) + "<br />")
    f_result.write("True Positive: " + str(lines[1].rstrip()) + "<br />")
    f_result.write("False Positive: " + str(lines[2].rstrip()) + "<br />")
    f_result.write("True Negative: " + str(lines[3].rstrip()) + "<br />")
    f_result.write("False Negative: " + str(lines[4].rstrip()) + "<br />")
    f_result.write("F1: " + str(lines[5].rstrip()) + "<br />")
    f_result.write("Accuracy: " + str(lines[6].rstrip()) + "<br />")
    f_result.write("Precision: " + str(lines[7].rstrip()) + "<br />")
    f_result.write("Recall: " + str(lines[7].rstrip()) + "<br />")
    f_result.write("<br /><br /><br />\n</body>\n</html>")
    f_result.close()
    
    return render_template("complete.html")
