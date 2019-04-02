#this file will serve to generate the initial model, and could be retooled
#to serve as a model "updater", i.e. generating a new model any time
#we gain access to a new labeled data set
#It also saves the model to a file so that we don't have to regenerate
#the model each time we want to use it to classify new data

from read_data import read
from split_data import split
from sklearn import svm
from joblib import dump
from test_model import run_metrics_model, F1, read_model_from_file
import os

def first_model():

    #We're going to keep track of the model # and files used
    #to train it in a file called list.txt, which will reside
    #in our data subdirectory
    flist = open("./data/list.txt", "w")
    flist.write("data_151.csv\ndata_130.csv\ndata_53.csv\n")
    flist.close

    data = read("data_151.csv")
    data += read("data_130.csv") + read("data_53.csv")
    features_training, labels_training, features_testing, labels_testing = split(data)

    #create SVM model
    svm_model = svm.SVC(max_iter = 10000, kernel='rbf', gamma = 'auto'  )
    svm_model.fit(features_training, labels_training.ravel())

    dump(svm_model, 'newmodel.joblib')

    #svm_model=read_model_from_file()

    TP, FP, TN, FN = run_metrics_model(svm_model, features_testing, labels_testing)
    f1 = F1(TP, FP, TN, FN)
    print('Coord_x|Coord_y|ISOS_z|ISOS_Size_x|ISOS_Size_y|COST_z|COST_Size_x|COST_Size_y ')
    #print(svm_model.coef_)
    print('F1 score = ' + str(f1))

def retrain_model(new_files):
    #open list.txt, add newest filename to the end
    flist = open("./data/list.txt", "a")
    for file in new_files:
        flist.write(file + "\n")
    flist.close

    with open("./data/list.txt") as flist:
        lines = flist.readlines()

    lines[0] = lines[0].rstrip()
    data = read(lines[0])

    #need to make sure we have the 3 starting datasets in the ./data
    #directory, and need to reference that with ./data
    for i in range(1,len(lines)):
        lines[i] = lines[i].rstrip()
        data += read("./data/" + lines[i])

    features_training, labels_training, features_testing, labels_testing = split(data)

    #create SVC model
    svm_model = svm.SVC(max_iter = 10000, kernel='rbf', gamma = 'auto'  )
    svm_model.fit(features_training, labels_training.ravel())

    #delete oldmodel.joblib, set current newmodel.joblib to old
    #then save new as newmodel.joblib
    try:
        os.remove("oldmodel.joblib")
    except:
        print("no oldmodel")
    os.rename("newmodel.joblib", "oldmodel.joblib")

    dump(svm_model, "newmodel.joblib")

    #svm_model=read_model_from_file()

    TP, FP, TN, FN = run_metrics_model(svm_model, features_testing, labels_testing)
    f1 = F1(TP, FP, TN, FN)
    #print('Coord_x|Coord_y|ISOS_z|ISOS_Size_x|ISOS_Size_y|COST_z|COST_Size_x|COST_Size_y ')
    #print(svm_model.coef_)
    print('F1 score = ' + str(f1))

    f_result = open("./templates/complete_retrain.html", "w")
    f_result.write("")
    f_result.close
    f_result = open("./templates/complete_retrain.html", "a")
    f_result.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<meta charset=\"UTF-8\">\n\t<title>Title</title>\n</head>\n<body>")
    f_result.write("TP: " + str(TP) + "<br />FP: " + str(FP) + 
    "<br />TN: " + str(TN) + "<br />FN: " + str(FN) + "<br />")
    f_result.write("F1: " + str(f1) + "<br />")
    f_result.write("\n</body>\n</html>")
    f_result.close()